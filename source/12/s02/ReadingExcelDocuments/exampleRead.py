import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))

print("=" * 10)

wb.get_sheet_names()
sheet = wb / get_sheet_by_name("Sheet3")
print(sheet)
print(type(sheet))
print(sheep.title)
anotherSheet = wb.get_active_sheet()
print(anotherSheet)
