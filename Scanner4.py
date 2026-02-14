# Date: 14-Feb-2026
# =====================================================


import cv2
import os
import numpy as np


# -----------------------------------------------------
# Welcome Message
# -----------------------------------------------------
def welcome():
    print("="*60)

    print("=" * 60)
    print(" SMART DOCUMENT SCANNER SYSTEM ")
    print("="*60)
    print()
    print("=" * 60)
    print("Sampling & Quantization Analysis\n")


# -----------------------------------------------------
# Load and Preprocess Image
# -----------------------------------------------------
def load_image(path):

    img = cv2.imread(path)
    image = cv2.imread(path)

    if img is None:
    if image is None:
        print("Error: Cannot load image ->", path)
        return None, None

    img = cv2.resize(img, (512, 512))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Resize to standard size
    image = cv2.resize(image, (512, 512))

    # Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return img, gray
    return image, gray


# Sampling
# -----------------------------------------------------
# Sampling (Resolution Reduction)
# -----------------------------------------------------
def sampling(gray):

    # High Resolution (Original)
    high = cv2.resize(gray, (512, 512))

    med = cv2.resize(gray, (256, 256))
    med = cv2.resize(med, (512, 512))
    # Medium Resolution
    medium = cv2.resize(gray, (256, 256))
    medium = cv2.resize(medium, (512, 512))

    # Low Resolution
    low = cv2.resize(gray, (128, 128))
    low = cv2.resize(low, (512, 512))

    return high, med, low
    return high, medium, low


# -----------------------------------------------------
# Quantization (Gray Level Reduction)
# -----------------------------------------------------
def quantize(image, levels):

    step = 256 // levels

    quantized = (image // step) * step

    return quantized.astype(np.uint8)


# -----------------------------------------------------
# Main Program
# -----------------------------------------------------
def main():

    welcome()

    files = os.listdir("images")
    image_folder = "images"

    # Check folder
    if not os.path.exists(image_folder):
        print("Images folder not found!")
        return

    files = os.listdir(image_folder)

    if len(files) == 0:
        print("No images found in images folder.")
        return

    for file in files:

        path = "images/" + file
        print("Processing:", file)

        img, gray = load_image(path)
        path = os.path.join(image_folder, file)

        if img is None:
        # Load image
        original, gray = load_image(path)

        if original is None:
            continue

        high, med, low = sampling(gray)
        # ---------------- Sampling ----------------
        high, medium, low = sampling(gray)

        # ---------------- Quantization ----------------
        q8 = quantize(gray, 256)   # 8-bit
        q4 = quantize(gray, 16)    # 4-bit
        q2 = quantize(gray, 4)     # 2-bit

        # ---------------- Display ----------------

        cv2.imshow("Original", original)
        cv2.imshow("Grayscale", gray)

        cv2.imshow("High Resolution (512x512)", high)
        cv2.imshow("Medium Resolution (256x256)", medium)
        cv2.imshow("Low Resolution (128x128)", low)

        cv2.imshow("8-bit Quantization", q8)
        cv2.imshow("4-bit Quantization", q4)
        cv2.imshow("2-bit Quantization", q2)

        cv2.imshow("High", high)
        cv2.imshow("Medium", med)
        cv2.imshow("Low", low)
        print("Showing results... Press any key")

        cv2.waitKey(2000)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# -----------------------------------------------------
# Program Entry
# -----------------------------------------------------
if __name__ == "__main__":
    main()
