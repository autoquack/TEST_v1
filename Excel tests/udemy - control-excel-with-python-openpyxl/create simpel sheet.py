from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save("C:\\Users\martin.haluska\Downloads\pythonTestFolder//" + "hello_world_2.xlsx")