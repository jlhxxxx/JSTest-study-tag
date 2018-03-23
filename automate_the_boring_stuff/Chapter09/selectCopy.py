#! python3
# selectCopy.py - scan the folder and copy all pdf to a new folder

import os, shutil

ext = ['png', 'pdf']
fromDir = 'C:\\Users\\Administrator\\Desktop\\test'
toDir = 'C:\\Users\\Administrator\\Desktop\\new'
os.makedirs(toDir, exist_ok=True)

for foldername, subfolders, filenames in os.walk(fromDir):
    for filename in filenames:
        if filename.split('.')[-1].lower() in ext:
            fromName = os.path.join(foldername, filename)
            toName = os.path.join(toDir, filename)
            print('move %s to %s...' % (fromName, toName))
            shutil.copy(fromName, toName)
print('done')
