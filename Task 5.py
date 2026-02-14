import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------
@@ -18,9 +19,18 @@
def welcome():

    print("=" * 60)
    print(" SMART DOCUMENT SCANNER SYSTEM ")
    print(" SMART DOCUMENT SCANNER & QUALITY ANALYSIS ")
    print("=" * 60)
    print("Sampling & Quantization Analysis\n")
    print("Final System with Sampling & Quantization\n")


# -----------------------------------------------------
# Create Output Folder
# -----------------------------------------------------
def create_output_folder():

    if not os.path.exists("outputs"):
        os.makedirs("outputs")


# -----------------------------------------------------
@@ -34,7 +44,7 @@ def load_image(path):
        print("Error: Cannot load image ->", path)
        return None, None

    # Resize to standard size
    # Resize
    image = cv2.resize(image, (512, 512))

    # Convert to Grayscale
@@ -48,14 +58,11 @@ def load_image(path):
# -----------------------------------------------------
def sampling(gray):

    # High Resolution (Original)
    high = cv2.resize(gray, (512, 512))

    # Medium Resolution
    medium = cv2.resize(gray, (256, 256))
    medium = cv2.resize(medium, (512, 512))

    # Low Resolution
    low = cv2.resize(gray, (128, 128))
    low = cv2.resize(low, (512, 512))

@@ -75,62 +82,143 @@ def quantize(image, levels):


# -----------------------------------------------------
# Main Program
# Print Observations
# -----------------------------------------------------
def print_observations():

    print("\n========== QUALITY OBSERVATION ==========")

    print("\n1. Text Clarity:")
    print("- High resolution images preserve sharp characters.")
    print("- Low resolution loses fine details.")

    print("\n2. Readability:")
    print("- 8-bit images are clear and readable.")
    print("- 4-bit images show banding effect.")
    print("- 2-bit images are heavily distorted.")

    print("\n3. OCR Suitability:")
    print("- Best: 512x512 + 8-bit.")
    print("- Worst: 128x128 + 2-bit.")

    print("========================================")


# -----------------------------------------------------
# Display & Save Comparison
# -----------------------------------------------------
def show_and_save(original, gray,
                  high, medium, low,
                  q8, q4, q2,
                  name):

    fig, ax = plt.subplots(3, 3, figsize=(12, 12))

    # Row 1
    ax[0, 0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    ax[0, 0].set_title("Original")

    ax[0, 1].imshow(gray, cmap="gray")
    ax[0, 1].set_title("Grayscale")

    ax[0, 2].imshow(high, cmap="gray")
    ax[0, 2].set_title("512x512")

    # Row 2
    ax[1, 0].imshow(medium, cmap="gray")
    ax[1, 0].set_title("256x256")

    ax[1, 1].imshow(low, cmap="gray")
    ax[1, 1].set_title("128x128")

    ax[1, 2].imshow(q8, cmap="gray")
    ax[1, 2].set_title("8-bit")

    # Row 3
    ax[2, 0].imshow(q4, cmap="gray")
    ax[2, 0].set_title("4-bit")

    ax[2, 1].imshow(q2, cmap="gray")
    ax[2, 1].set_title("2-bit")

    ax[2, 2].axis("off")

    # Remove axes
    for i in range(3):
        for j in range(3):
            ax[i, j].axis("off")

    plt.suptitle("Document Quality Comparison", fontsize=16)

    filename = f"outputs/{name}_comparison.png"

    plt.savefig(filename)
    plt.show()

    print("Saved:", filename)


# -----------------------------------------------------
# Main Function
# -----------------------------------------------------
def main():

    welcome()

    create_output_folder()

    image_folder = "images"

    # Check folder
    if not os.path.exists(image_folder):
        print("Images folder not found!")
        return

    files = os.listdir(image_folder)

    if len(files) == 0:
        print("No images found in images folder.")
        print("No images found!")
        return

    for file in files:

        print("Processing:", file)
        print("\nProcessing:", file)

        path = os.path.join(image_folder, file)

        # Load image
        original, gray = load_image(path)

        if original is None:
            continue

        # ---------------- Sampling ----------------
        # -------- Sampling --------
        high, medium, low = sampling(gray)

        # ---------------- Quantization ----------------
        q8 = quantize(gray, 256)   # 8-bit
        q4 = quantize(gray, 16)    # 4-bit
        q2 = quantize(gray, 4)     # 2-bit

        # ---------------- Display ----------------
        # -------- Quantization --------
        q8 = quantize(gray, 256)
        q4 = quantize(gray, 16)
        q2 = quantize(gray, 4)

        cv2.imshow("Original", original)
        cv2.imshow("Grayscale", gray)
        # -------- Save Outputs --------
        name = file.split(".")[0]

        cv2.imshow("High Resolution (512x512)", high)
        cv2.imshow("Medium Resolution (256x256)", medium)
        cv2.imshow("Low Resolution (128x128)", low)
        cv2.imwrite(f"outputs/{name}_gray.png", gray)
        cv2.imwrite(f"outputs/{name}_512.png", high)
        cv2.imwrite(f"outputs/{name}_256.png", medium)
        cv2.imwrite(f"outputs/{name}_128.png", low)
        cv2.imwrite(f"outputs/{name}_8bit.png", q8)
        cv2.imwrite(f"outputs/{name}_4bit.png", q4)
        cv2.imwrite(f"outputs/{name}_2bit.png", q2)

        cv2.imshow("8-bit Quantization", q8)
        cv2.imshow("4-bit Quantization", q4)
        cv2.imshow("2-bit Quantization", q2)
        # -------- Comparison Figure --------
        show_and_save(original, gray,
                      high, medium, low,
                      q8, q4, q2,
                      name)

        print("Showing results... Press any key")
    # -------- Final Observations --------
    print_observations()

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    print("\nAll tasks completed successfully!")


# -----------------------------------------------------
