import openpyxl

wb = openpyxl.Workbook()
sheet = wb["Sheet"]
sheet["A1"] = "Hello World"
print(sheet["A1"].value)
