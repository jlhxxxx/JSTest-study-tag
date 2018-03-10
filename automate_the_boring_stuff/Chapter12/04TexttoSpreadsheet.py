#! python3
# TexttoSpreadsheet.py - there have a bug that the cells can't store strings(only apply numbers)

import openpyxl, sys, os


try:
    file = sys.argv[1]
except: 
    file = 'table.txt'

readFile = open(file)
date = readFile.readlines()
readFile.close()

wb = openpyxl.Workbook()
sheet = wb.active

for rowObj in range(1, len(date)+1):
    rowDate = date[rowObj-1][:-1].split(',')
    for columnObj in range(1, len(rowDate)+1):
        c = sheet.cell(row=rowObj, column=columnObj)
        c.value = rowDate[columnObj-1]
        print(c.value)

wb.save('table.xlsx')
print('done')