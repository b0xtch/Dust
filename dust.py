import sys
import glob, os
import numpy as np
import pandas as pd
from atom import Atom

def main(images, weather):
    '''
    The main entry of dust
    '''
    weather = Atom(weather, images)

if __name__=='__main__':
#     images = sys.argv[1]
#     weather = sys.argv[2]
    images = 'images'
    weather = 'weather'
    main(images, weather)
