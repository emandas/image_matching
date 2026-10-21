# Image Contour & Hu Moments Comparator

A simple Python script utilizing **OpenCV** to compare two images based on their structural shapes using image moments and **Hu Moments** (translation, scale, and rotation invariant shape descriptors).

---

## Overview

This script executes the following workflow:
1. Prompts the user for the absolute file paths of two images.
2. Loads the images in **grayscale**.
3. Applies a **binary inverse threshold** (threshold value: `150`) to separate the foreground shapes from the background.
4. Detects contours using OpenCV's `cv2.findContours` function.
5. Computes raw image moments and Hu Moments for the second detected contour (`contours[1]`) of both images.
6. Compares the Hu Moment features and outputs whether the shapes match.

---

## Prerequisites

Ensure you have Python and OpenCV installed on your system. You can install OpenCV via pip:

```bash
pip install opencv-python
```

---

## Usage

1. Run the script in your terminal:
   ```bash
   python script.py
   ```
2. Enter the absolute path to the first image when prompted:
   ```text
   Enter img1's absolute path : /path/to/your/image1.png
   ```
3. Enter the absolute path to the second image:
   ```text
   Enter img2's absolute path : /path/to/your/image2.png
   ```
4. Review the console output, which prints the calculated moments, Hu moment vectors, and the final match verdict (`images match` or `images not match`).

---


## Code Breakdown

* **`cv2.imread(..., 0)`**: Reads the images directly in grayscale mode.
* **`cv2.threshold(..., cv2.THRESH_BINARY_INV)`**: Converts grayscale pixels into binary (black and white) values inverted for contour tracing.
* **`cv2.findContours`**: Retrieves object outlines from the thresholded binary image.
* **`cv2.HuMoments`**: Computes a set of 7 scale-, rotation-, and translation-invariant Hu moments derived from central image moments for `contours[1]`.

---

## Limitations & Considerations

* **Contour Dependency**: The script assumes that the target shape resides at index `1` (`contours[1]`). Images with fewer than two contours will cause an `IndexError`.
* **Floating-Point Comparison**: The script uses strict equality (`==`) to compare floating-point Hu moments. Due to floating-point precision variations, strict equality can occasionally fail for identical shapes. For production-grade shape matching, consider using OpenCV's built-in `cv2.matchShapes()` function instead.
