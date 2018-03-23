#! python3
# fillGaps.py - finds all files with a given prefix which have some gaps and rename all the later files to close this gap.

import os, shutil

searchDir = 'C:\\Users\\Administrator\\Desktop\\test'
os.chdir(searchDir)

count = 1000
fileList = [x for x in os.listdir('.') if x.startswith('spam') and x.endswith('.txt')]
for file in fileList:
    count += 1
    cut = file[4:][:-4]
    if int(cut)+1000 != count or len(cut) != 3:
        shutil.move(file, 'spam' + str(count)[1:] + '.txt')
print('done')


