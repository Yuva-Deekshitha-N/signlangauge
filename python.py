import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/image/collectedimages'
labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    # Create the folder for each label if it doesn't exist
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)

    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)

    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, f'{label}.{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        # Break if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()
