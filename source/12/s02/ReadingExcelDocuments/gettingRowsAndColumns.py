import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
sheet = wb["Sheet1"]
print(tuple(sheet["A1": "C3"]))

for rowOfCellObjects in sheet["A1": "C3"]:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print("--- END OF ROW ---")

sheetCurrent = wb.active
print(tuple(sheetCurrent.columns)[1])

for cellObj in tuple(sheetCurrent.columns)[1]:
    print(cellObj.value)
