from path import Path
import itertools
import cv2
import numpy as np
import glob
temp = [i.files()  for i in  Path('DAVIS/JPEGImages/480p/').listdir()]
for i in range(len(temp)):
    temp[i] = sorted(temp[i])
flattened_list  = list(itertools.chain(*temp))
img = cv2.imread(flattened_list[0])
height, width, layers = img.shape
size = (width,height)

# fourcc = cv2.VideoWriter_fourcc("H.264")

out = cv2.VideoWriter('videos/project23.mp4',cv2.VideoWriter_fourcc(*"mp4v"), 15, size)

img_array = []
for filename in flattened_list[:60]:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    
for i in range(len(img_array)):
    out.write(img_array[i])

# img_array = []
# for filename in flattened_list[2000:4000]:
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)

# for i in range(len(img_array)):
#     out.write(img_array[i])
    
# img_array = []
# for filename in flattened_list[4000:6000]:
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)

# for i in range(len(img_array)):
#     out.write(img_array[i])


# img_array = []
# for filename in flattened_list[6000:]:
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)

# for i in range(len(img_array)):
#     out.write(img_array[i])
    

cv2.destroyAllWindows()

out.release()    