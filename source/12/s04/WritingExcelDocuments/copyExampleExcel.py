import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
sheet = wb.get_active_sheet()
sheet.title = "Spam Spam Spam"
print(wb.get_sheet_names())
wb.save("example_copy.xlsx")
