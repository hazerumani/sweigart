import openpyxl

wb = openpyxl.load_workbook("merged.xlsx")
sheet = wb.get_active_sheet()
sheet.unmerge("A1:D3")
sheet.unmerge("C5:D5")
wb.save("merged.xlsx")
