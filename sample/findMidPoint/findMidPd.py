
# Original include is like below
#from imgDetectPosition import findMidPoint

# how to run the script , example
# python3 findMidPd.py LConer.png RConer.png

'''
my_project/
│
├── sample/
│   ├── findMidPoint/
│   │   └── findMidPd.py
│   │
│   └── .../
│       └── ....py
│
└── lib/
    ├── __init__.py
    └── imgDetectPosition.py
'''
# sample/findMidPoint/findMidPd.py

import sys
import os

# Add the path to my_library to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lib')))

from imgDetectPosition import findMidPoint

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find multiple images on the screen and calculate the midpoint.")
    parser.add_argument("image_paths", nargs='+', help="Paths to the image files (e.g., image1.png image2.png ...)")

    args = parser.parse_args()
    findMidPoint(args.image_paths)