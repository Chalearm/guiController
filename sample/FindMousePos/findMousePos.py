# Original include is like below
#from ../lib/mouseController import get_current_mouse_position



'''
my_project/
│
├── sample/
│   ├── FindMousePos/
│   │   └── findMousePos.py
│   │
│   └── .../
│       └── ....py
│
└── lib/
    ├── __init__.py
    └── mouseController.py
'''
# sample/FindMousePos/findMousePos.py

import sys
import os

# Add the path to my_library to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib')))

from mouseController import get_current_mouse_position  # Import the function from module.py



# Example usage
if __name__ == "__main__":
    position = get_current_mouse_position()
    print(f"Current mouse position: {position}")