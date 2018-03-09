#! python3
# passwordBreaker.py - use a dict try to decrypt the PDFs

import PyPDF2, os

#  D:/work/Workspaces/MYGitHub/Programing/automate_the_boring_stuff/Chapter13/
readFile = open('dictionary.txt')
dicts = readFile.readlines()
readFile.close()

pdfFile = 'encrypted.pdf'
pdfReader = PyPDF2.PdfFileReader(open(pdfFile, 'rb'))

if pdfReader.isEncrypted:
    findout = 0
    print('the %s is encrypted.' % pdfFile)
    for word in dicts:
        if pdfReader.decrypt(word[:-1].lower()):
            print('the password is %s.' % word[:-1].lower())
            findout = 1
            break
        elif pdfReader.decrypt(word[:-1]):
            print('the password is %s.' % word[:-1])
            findout = 1
            break
    if findout == 0:
        print('cant find the password.')   
else:
    print('the %s is not encrypted.' % pdfFile)