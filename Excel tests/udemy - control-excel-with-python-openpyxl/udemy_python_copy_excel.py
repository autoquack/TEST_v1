from openpyxl import load_workbook
wb = load_workbook("Added_sheets.xlsx")
for sheet in wb:
    print(sheet.title)

source = wb("New title")
new_sheet = wb.copy_worksheet(source)
new_sheet.title = "copied new title"
for sheet in wb:
    print(sheet.title)

wb.save("Copied_sheet.xlsx")