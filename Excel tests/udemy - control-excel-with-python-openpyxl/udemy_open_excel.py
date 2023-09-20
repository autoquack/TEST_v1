import openpyxl

wb = openpyxl.load_workbook("text123.xlsx")
for sheet in wb:
    print(sheet.title)