# mouseController.py
import pyautogui
import time

def get_current_mouse_position():
    """
    Get the current position of the mouse cursor.

    Returns:
    tuple: (x, y) coordinates of the current mouse position.
    """
    x, y = pyautogui.position()
    return (x, y)

def click_mouse(x, y, button='left', duration=0, clicks=1):
    """
    Move the mouse to the specified coordinates and click.

    Parameters:
    x (int): The x-coordinate on the screen.
    y (int): The y-coordinate on the screen.
    button (str): 'left' for left-click, 'right' for right-click.
    duration (float): Duration to move the mouse.
    clicks (int): Number of clicks to perform.
    """
    # Move the mouse to the specified position
    pyautogui.moveTo(x, y, duration)
    
    # Perform the specified number of clicks
    for _ in range(clicks):
        pyautogui.click(button=button)
        time.sleep(0.1)  # Optional delay between clicks