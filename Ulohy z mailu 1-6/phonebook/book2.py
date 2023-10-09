
from openpyxl import load_workbook

wb_append = load_workbook("C:\\Users\\martin.haluska\\PycharmProjects\\TEST_v1\\Ulohy z mailu 1-6\\phonebook\\phonebook.xlsx")

search_input = input("Hladaj: ")
name = None
age = None
country = None

for row in excel_sheet.rows:
    if search_input in row[0:3].value:
        name = row[0].value
        age = row[1].value
        country = row[2].value
        break