#import argparse
import cv2
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())
image = cv2.imread("/Users/vanshika/Downloads/Flicker8k_Dataset/1000268201_693b08cb0e.jpg")
cv2.imshow("image", image)
cv2.waitKey(0)
