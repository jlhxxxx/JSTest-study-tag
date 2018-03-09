#! python3
# excelToCsv.py
# D:/work/Workspaces/MYGitHub/Programing/automate_the_boring_stuff/Chapter14/
import os, openpyxl, csv
for excelFile in os.listdir('./sheets'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue

    wb = openpyxl.load_workbook('./sheets/'+ excelFile)
    for sheetName in wb.sheetnames:
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]

        # Create the CSV filename from the Excel filename and sheet title.
        os.makedirs('./csvs', exist_ok=True)
        outputPath = os.path.join('./csvs', excelFile[:-5] + '_' + sheetName + '.csv')
        print('creat ' + outputPath)
        outputFile = open(outputPath, 'w', newline='')
        # Create the csv.writer object for this CSV file.
        outputWriter = csv.writer(outputFile)
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                # Append each cell's data to rowData.
                rowData.append(str(sheet.cell(row=rowNum, column=colNum).value))
            # Write the rowData list to the CSV file.
            outputWriter.writerow(rowData)
        outputFile.close()
print('done')