mkdir -p video_files

container_name=project11.mp4

# Download video sample
wget -q -O ${container_name} https://download.blender.org/durian/trailer/sintel_trailer-720p.mp4

IFS='.' read -a splitted <<< "$container_name"

for i in {0..4};
do
    ffmpeg -ss 00:00:${i}0 -t 00:00:10 -i $container_name -vcodec copy -acodec copy -y video_files/${splitted[0]}_$i.${splitted[1]
}
done
