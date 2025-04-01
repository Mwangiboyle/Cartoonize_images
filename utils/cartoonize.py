import cv2
import numpy as np

def cartoonize_image(img: np.ndarray) -> np.ndarray:
    """Process image array and return cartoonized version"""
    if img is None:
        raise ValueError("Failed to load image.")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color = cv2.bilateralFilter(img, 9,300,300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    #cartoon_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    return cartoon

