import openpyxl
from openpyxl.styles import Font, Style

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

fontObj1 = Font(name='Times New Roman', bold=True)
styleObj1 = Style(font=fontObj1)
sheet['A1'].style / styleObj
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
styleObj2 = Style(font=fontObj2)
sheet['B3'].style / styleObj
sheet['B3'] = '24 pt Italic'

wb.save('styles.xlsx')
