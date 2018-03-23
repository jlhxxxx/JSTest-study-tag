#! python3
# madLibs.py - reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import os, re

replaceRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
file = 'lovestory.txt'
readFile = open(file)
text = readFile.read()
print(text)
replaceList = replaceRegex.findall(text)
for i in replaceList:
    if i == 'ADJECTIVE':
        word = input('please enter an adjective:')
    else:
        word = input('please enter a %s:' % i.lower())
    text = replaceRegex.sub(word, text, 1)

newFile = open('lovestory2.txt', 'w')
newFile.write(text)
print('done')