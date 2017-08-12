#!/usr/bin/python3

import os
import cv2
import argparse


def resize_folder(folder, width, height):
    for file in os.listdir(folder):
        filename = os.path.join(folder, file)
        if os.path.isdir(filename):
            resize_folder(filename, width, height)
        else:
            resize_image(filename, width, height)


def resize_image(filename, width, height):
    img = cv2.imread(filename)

    if img is None:
        print('Skipping over non-image %s.' % filename)
        return

    if width.find('.') != -1:
        final_width = img.shape[0]*float(width)
    else:
        final_width = int(width)

    if height.find('.') != -1:
        final_height = img.shape[0]*float(height)
    else:
        final_height = int(height)

    img = cv2.resize(img, (final_width, final_height))
    cv2.imwrite(filename, img)

    print('Resized %s to %dx%d.' % (filename, final_width, final_height))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('images', type=str, nargs='+')
    parser.add_argument('target_width', type=str)
    parser.add_argument('target_height', type=str)
    args = parser.parse_args()

    for file in args.images:
        filename = os.path.abspath(file)
        if os.path.isdir(filename):
            resize_folder(filename, args.target_width, args.target_height)
        else:
            resize_image(filename, args.target_width, args.target_height)