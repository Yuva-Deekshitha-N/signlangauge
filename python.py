import cv2
import os
import time
import uuid
IMAGES_PATH = 'Tensorflow/workspace/image/collectedimages'
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15
for labels in labels:
  !mkdir{'Tensorflow\workspace\image\collectedimages\\'+label}
  cap = cv2.Videocapture(0)
  print('Collecting images for {}'.format(label))
  time.sleep(5)
  for imgnum in range(number_imgs):
    ret, frame = cap.read()
    imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    time.sleep(2)

    if cv2.waitKey(1) && 0xFF == ord('q'):
      break
  cap.release()

  
  
  
