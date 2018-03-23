#! python3 
# findLargeFolder.py - find folders larger than 100M

import os

searchDir = 'D:\\迅雷下载'

for foldername, subfolders, filenames in os.walk(searchDir):
    for filename in filenames:
        file = os.path.join(foldername, filename)
        if os.path.getsize(file) > 1024*1024*100:
            print(file)
print('done')
