"""
`freeze_panes` — setting Rows and columns frozen
`sheet.freeze_panes = 'A2'` — Row 1
`sheet.freeze_panes = 'B1'` — Column A
`sheet.freeze_panes = 'C1'` — Columns A and B
`sheet.freeze_panes = 'C2'` — Row 1 and columns A and B
`sheet.freeze_panes = 'A1'` or `sheet.freeze_panes` = None No frozen panes
"""

import openpyxl

wb = openpyxl.load_workbook("produceSales.xlsx")
sheet = wb.active
sheet.freeze_panes = "A2"
wb.save("freezeExample.xlsx")
