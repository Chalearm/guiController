
# Original include is like below
#from imgDetectPosition import find_image, calculate_center, convertPosToRealPos



'''
my_project/
│
├── sample/
│   ├── DetectAnImg/
│   │   └── DetectAnImg.py
│   │
│   └── .../
│       └── ....py
│
└── lib/
    ├── __init__.py
    └── imgDetectPosition.py
'''
# sample/DetectAnImg/DetectAnImg.py

import sys
import os

# Add the path to my_library to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib')))

from imgDetectPosition import find_image, calculate_center, convertPosToRealPos



# Example usage
if __name__ == "__main__":
    image_file = 'B1.png'  # Replace with the path to your PNG file
    position = find_image(image_file)
    print(position)