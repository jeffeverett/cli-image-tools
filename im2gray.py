#!/bin/python3

import cv2
import sys
import os

def convert_to_grayscale(img_file):
    try:
        img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise Exception('Could not open specified file.')
        cv2.imwrite(img_file, img)
        print('Converted %s to grayscale.' % (img_file,))
    except Exception as e:
        print('Error while processing %s. %s' % (img_file, str(e)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('One or more files must be specified.')
        exit()

    for file in sys.argv[1:]:
        if os.path.isdir(file):
            for img in os.listdir(file):
                img = os.path.join(file, img)
                convert_to_grayscale(img)
        else:
            convert_to_grayscale(file)