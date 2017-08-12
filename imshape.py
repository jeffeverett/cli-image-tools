#!/bin/python3

import cv2
import sys
import os

def imshape(img_file):
    img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise Exception('Could not open specified file.')
    return img.shape

def print_imshape(img_file):
    try:
        print('%s has dimensions: %s' % (img_file, str(imshape(img_file))))
    except Exception as e:
        print('Error while processing %s. %s' % (img_file, str(e)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('One or more files must be specified.')
        exit()

    for file in sys.argv[1:]:
        if os.path.isdir(file):
            for img in os.listdir(file):
                print_imshape(img)
        else:
            print_imshape(file)