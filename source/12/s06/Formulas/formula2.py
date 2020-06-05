import openpyxl

wbFormulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wbFormulas.get_active_sheet()
sheet['A3'].value
wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
sheet = wbDataOnly.get_active_sheet()
sheet['A3'].value
