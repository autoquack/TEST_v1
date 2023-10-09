from openpyxl import Workbook

### definovanie noveho prazdneho workbooku bez mena ###
wb = Workbook()

### otvorenie aktivneho sheetu ###
ws = wb.active
### definovanie nazvu aktivneho worksheetu ###
ws.title = "Data"
### pripisanie hodnot do daneho aktivneho sheetu ###
ws.append(["Alpha A1", "Beta B1", "Gamma C1"])
ws.append(["Alpha A2", "Beta B2","Gamma C2"])

### ulozi novy workbook pod danym menom ###
wb.save("test_vytvorenie_noveho_workbooku_2.xlsx")
