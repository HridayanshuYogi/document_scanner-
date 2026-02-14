import cv2
import os
import numpy as np


# Header
def welcome():
    print("="*60)
    print(" SMART DOCUMENT SCANNER SYSTEM ")
    print("="*60)
    print("Analyzing Sampling & Quantization Effects\n")
    print()


# Load Image
def load_image(path):

    img = cv2.imread(path)

    if img is None:
        print("Image not found:", path)
        return None, None

    img = cv2.resize(img, (512, 512))
@@ -35,24 +33,40 @@ def load_image(path):
    return img, gray


# Sampling
def sampling(gray):

    high = cv2.resize(gray, (512, 512))

    med = cv2.resize(gray, (256, 256))
    med = cv2.resize(med, (512, 512))

    low = cv2.resize(gray, (128, 128))
    low = cv2.resize(low, (512, 512))

    return high, med, low


def main():

    welcome()

    folder = "images"
    files = os.listdir(folder)
    files = os.listdir("images")

    for file in files:

        path = os.path.join(folder, file)
        path = "images/" + file

        img, gray = load_image(path)

        if img is None:
            continue

        cv2.imshow("Original", img)
        cv2.imshow("Grayscale", gray)
        high, med, low = sampling(gray)

        cv2.imshow("High", high)
        cv2.imshow("Medium", med)
        cv2.imshow("Low", low)

        cv2.waitKey(2000)
        cv2.destroyAllWindows()
