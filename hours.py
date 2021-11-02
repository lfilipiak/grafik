import openpyxl
import os


wb = openpyxl.load_workbook("2021 STYCZEŃ.xlsx")
print(wb.sheetnames)
sheet = wb.active
# sheet.cell(2, 2, value=123)
wb.save("2021 STYCZEŃ.xlsx")
