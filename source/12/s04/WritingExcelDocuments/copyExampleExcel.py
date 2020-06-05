import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
sheet = wb.active
sheet.title = "Spam Spam Spam"
print(wb.sheetnames)
wb.save("example_copy.xlsx")
