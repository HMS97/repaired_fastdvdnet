import cv2
print(cv2.__version__)
for file_path in ['gopro_540p/hypersmooth/hypersmooth.avi','gopro_540p/motorbike/motorbike.avi',
    'gopro_540p/rafting/rafting.avi','gopro_540p/snowboard/snowboard.avi']:
  vidcap = cv2.VideoCapture(file_path)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite(f"testimages/{file_path.split('/')[1]}/frame%d.jpg" % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    count += 1