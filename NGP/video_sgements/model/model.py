

import torch
from torch.cuda.amp import autocast as autocast
import torch.nn as nn
from eva_vit import Trans_Block

try:
    from .blip2 import Blip2Base, disabled_train
except:
    from blip2 import Blip2Base, disabled_train


class VSeg(Blip2Base):
    """
    VideoChat model.
    """
    def __init__(self, config):
        super().__init__()


        self.tokenizer = self.init_tokenizer()
        self.low_resource = config.low_resource

        self.vit_precision = config.vit_precision
        print(f'Loading VIT. Use fp16: {config.vit_precision}')
        self.visual_encoder, self.ln_vision = self.init_vision_encoder(
            config.vit_model, config.img_size, config.drop_path_rate, 
            config.use_grad_checkpoint, config.vit_precision, config.vit_model_path,
            temporal_downsample=config.temporal_downsample,
            no_lmhra=config.no_lmhra, 
            double_lmhra=config.double_lmhra,
            lmhra_reduction=config.lmhra_reduction, 
            gmhra_layers=config.gmhra_layers, 
            gmhra_drop_path_rate=config.gmhra_drop_path_rate,
            gmhra_dropout=config.gmhra_dropout, 
        )
        if config.freeze_vit:
            print("freeze vision encoder")
            if not config.freeze_mhra:
                open_list = []
                for name, param in self.visual_encoder.named_parameters():
                    if 'mhra' not in name:
                        param.requires_grad = False
                    else:
                        open_list.append(name)

            else:
                for name, param in self.visual_encoder.named_parameters():
                    param.requires_grad = False
                self.visual_encoder = self.visual_encoder.eval()
                self.visual_encoder.train = disabled_train
                for name, param in self.ln_vision.named_parameters():
                    param.requires_grad = False
                self.ln_vision = self.ln_vision.eval()
                self.ln_vision.train = disabled_train
            
        self.blocks = nn.ModuleList([
                Trans_Block(dim = config.embedding_size, num_heads = config.embedding_size//88, mlp_ratio= 4.3637)
                    for i in range(10)])
        self.norm = nn.LayerNorm(config.embedding_size)
        self.fc_norm = nn.LayerNorm(config.embedding_size)

        self.head = nn.Linear(config.embedding_size, config.frames)
        self.score_head = nn.Linear(config.embedding_size, 1)
        self.max_txt_len = config.max_txt_len


    def vit_to_cpu(self):
        self.ln_vision.to("cpu")
        self.ln_vision.float()
        self.visual_encoder.to("cpu")
        self.visual_encoder.float()

    def forward_features(self, interval_1,interval_2):

        with self.maybe_autocast():
            T = interval_1.shape[1]
            # use_image = True if T == 1 else False
            interval_1 = interval_1.permute(0, 2, 1, 3, 4) # [B,T,C,H,W] -> [B,C,T,H,W]
            interval_2 = interval_2.permute(0, 2, 1, 3, 4) # [B,T,C,H,W] -> [B,C,T,H,W]
            interval1_embeds = self.ln_vision(self.visual_encoder(interval_1))
            interval2_embeds = self.ln_vision(self.visual_encoder(interval_2))
        x = torch.concat((interval1_embeds, interval2_embeds), dim=1)
        return x


            
    def forward(self, interval_1,interval_2, y = None):
        
        x = self.forward_features(interval_1,interval_2)
        x = self.norm(x)
        for block in self.blocks:
            x = block(x)
        x = x[:, 0]
        x = self.head(x)
        if y!= None:
            loss_fn = nn.BCEWithLogitsLoss()
            loss = loss_fn(x, y)
            return x, loss
        else:
            return x     