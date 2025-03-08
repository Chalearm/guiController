# Original include is like below
#from imgDetectPosition import find_image, calculate_center, convertPosToRealPos
#from mouseController import click_mouse



'''
my_project/
│
├── sample/
│   ├── FindPosAndClick/
│   │   └── findPositionAndClickLeft1.py
│   │
│   └── .../
│       └── ....py
│
└── lib/
    ├── __init__.py
    └── mouseController.py
    └── imgDetectPosition.py
'''
# sample/FindMousePos/findMousePos.py

import sys
import os

# Add the path to my_library to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib')))

from imgDetectPosition import find_image, calculate_center, convertPosToRealPos
from mouseController import click_mouse

if __name__ == "__main__":
    # Paths to the corner images
    left_corners_image = 'L1.png'  # Replace with your image path
    right_corners_image = 'R1.png'  # Replace with your image path

    # Find the corner images
    left_corner_position = find_image(left_corners_image)
    right_corner_position = find_image(right_corners_image)
    print(left_corner_position)
    print(right_corner_position)
    # Check if both corners were found
    if left_corner_position != (-1, -1) and right_corner_position != (-1, -1):
        # Calculate the center position between the two corners
        center_position_org = calculate_center({left_corner_position, right_corner_position})
        center_position = convertPosToRealPos(center_position_org[0], center_position_org[1], 0.5, 0.5)
        print(f"Center position: {center_position}")

        # Click at the center position
        click_mouse(center_position[0], center_position[1], button='left', duration=0.5, clicks=1)
    else:
        print("One or both images were not found.")