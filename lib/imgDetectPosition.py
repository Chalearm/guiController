import cv2
import numpy as np
import pyautogui
import time

def find_image_with_pyautogui(image_path):
    """
    Locate an image on the screen using pyautogui.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    tuple: (x, y) coordinates of the top-left corner of the located image,
           or (-1, -1) if not found.
    """
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)  # Confidence threshold for partial matches
        if location is not None:
            return (location.left, location.top)
        else:
            return (-1, -1)
    except Exception as e:
        print(f"An error occurred while finding the image with pyautogui: {e}")
        return (-1, -1)

def find_image_with_opencv(template_path):
    """
    Locate an image on the screen using OpenCV template matching.

    Parameters:
    template_path (str): Path to the template image file.

    Returns:
    tuple: (x, y) coordinates of the top-left corner of the located image,
           or (-1, -1) if not found.
    """
    # Take a screenshot
    screen = pyautogui.screenshot()
    # Convert the screenshot to a numpy array, then convert to BGR for OpenCV
    screen_bgr = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    # Read the template image
    template = cv2.imread(template_path)
    if template is None:
        print(f"Error loading template image at {template_path}")
        return (-1, -1)

    template_height, template_width = template.shape[:2]
    
    # Perform template matching
    result = cv2.matchTemplate(screen_bgr, template, cv2.TM_CCOEFF_NORMED)
    
    # Set a threshold for matching
    threshold = 0.8
    loc = np.where(result >= threshold)

    # If matches are found, return the first match's coordinates
    if loc[0].size > 0:
        x = loc[1][0]
        y = loc[0][0]
        return (x, y)

    return (-1, -1)

def find_image(image_path):
    """
    Locate an image on the screen, first using pyautogui and falling back to OpenCV if necessary.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    tuple: (x, y) coordinates of the located image,
           or (-1, -1) if not found.
    """
    # First try to find the image with pyautogui
    position = find_image_with_pyautogui(image_path)
    
    # If not found, try OpenCV
    if position == (-1, -1):
        print("Image not found with pyautogui, trying OpenCV.")
        position = find_image_with_opencv(image_path)
    
    return position

def convertPosToRealPos(x, y, factor_x, factor_y):
    """
    Convert (x, y) coordinates by applying specified factors.

    Parameters:
    x (float): The original x-coordinate.
    y (float): The original y-coordinate.
    factor_x (float): The factor to multiply the x-coordinate.
    factor_y (float): The factor to multiply the y-coordinate.

    Returns:
    tuple: (new_x, new_y) after applying the factors.
    """
    new_x = x * factor_x
    new_y = y * factor_y
    return new_x, new_y

import cv2
import numpy as np
import pyautogui
import argparse

def find_image_with_pyautogui(image_path):
    """
    Locate an image on the screen using pyautogui.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    tuple: (x, y) coordinates of the top-left corner of the located image,
           or (-1, -1) if not found.
    """
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=0.8)  # Confidence threshold for partial matches
        if location is not None:
            return (location.left, location.top)
        else:
            return (-1, -1)
    except Exception as e:
        print(f"An error occurred while finding the image with pyautogui: {e}")
        return (-1, -1)

def find_image_with_opencv(template_path):
    """
    Locate an image on the screen using OpenCV template matching.

    Parameters:
    template_path (str): Path to the template image file.

    Returns:
    tuple: (x, y) coordinates of the top-left corner of the located image,
           or (-1, -1) if not found.
    """
    # Take a screenshot
    screen = pyautogui.screenshot()
    # Convert the screenshot to a numpy array, then convert to BGR for OpenCV
    screen_bgr = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

    # Read the template image
    template = cv2.imread(template_path)
    if template is None:
        print(f"Error loading template image at {template_path}")
        return (-1, -1)

    template_height, template_width = template.shape[:2]
    
    # Perform template matching
    result = cv2.matchTemplate(screen_bgr, template, cv2.TM_CCOEFF_NORMED)
    
    # Set a threshold for matching
    threshold = 0.8
    loc = np.where(result >= threshold)

    # If matches are found, return the first match's coordinates
    if loc[0].size > 0:
        x = loc[1][0]
        y = loc[0][0]
        return (x, y)

    return (-1, -1)

def find_image(image_path):
    """
    Locate an image on the screen, first using pyautogui and falling back to OpenCV if necessary.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    tuple: (x, y) coordinates of the located image,
           or (-1, -1) if not found.
    """
    # First try to find the image with pyautogui
    position = find_image_with_pyautogui(image_path)
    
    # If not found, try OpenCV
    if position == (-1, -1):
        print("Image not found with pyautogui, trying OpenCV.")
        position = find_image_with_opencv(image_path)
    
    return position

def calculate_center(corners):
    """
    Calculate the center point of all corner points.

    Parameters:
    corners (list of tuples): List of (x, y) coordinates of the corners.

    Returns:
    tuple: (center_x, center_y) coordinates of the center point.
    """
    if not corners:
        return (-1, -1)
    
    x_total = sum(corner[0] for corner in corners)
    y_total = sum(corner[1] for corner in corners)
    num_points = len(corners)

    center_x = x_total // num_points
    center_y = y_total // num_points
    return (center_x, center_y)

def findMidPoint(image_paths):
    corner_positions = []

    for image_path in image_paths:
        position = find_image(image_path)
        if position != (-1, -1):
            corner_positions.append(position)
        else:
            print(f"Image not found: {image_path}")

    # Check if any corners were found
    if corner_positions:
        # Calculate the center position from the corners
        center_position = calculate_center(corner_positions)
        print(f"Midpoint of the images: {center_position}")

    else:
        print("No images were found.")