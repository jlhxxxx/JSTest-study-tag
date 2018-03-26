#! python3
# regFindAll.py - search for all txt in a folder by a regex which the user input

import os, re

match = input('please input a regex(without \'\'):')
searchRegex = re.compile(match)

searchDir = 'C:\\Users\\Administrator\\Desktop\\test'
os.chdir(searchDir)
for file in os.listdir('.'):
    if file.endswith('.txt'):
        readFile = open(file)
        for i, line in enumerate(readFile.readlines()):
            if searchRegex.search(line) is not None:
                if line.endswith('\n'):
                    line = line[:-1]
                print('find in line %s in %s: %s' % (i+1, file, line))
print('done')