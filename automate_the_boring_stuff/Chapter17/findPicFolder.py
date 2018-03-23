#! python3 
# findPicFolder.py - scan the entire disk and find picture folders

import os
from PIL import Image

PicEx = ['jpg', 'png', 'bmp', 'gif', 'jpeg']

for foldername, subfolders, filenames in os.walk('D:\\壁纸'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if filename.split('.')[-1].lower() not in PicEx:
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        checkIm = Image.open(os.path.join(foldername, filename))
        width, height = checkIm.size
        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles >= numNonPhotoFiles:
        print(foldername)
