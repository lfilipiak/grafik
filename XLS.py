import calendar
import datetime
from openpyxl.workbook import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter
import data


def month_to_csv(year=2021, month=1):
    """
    :param year: pobiera rok
    :param month: pobiera wartość miesiąca od 1 do 12
    :returns: zwraca plik z tabelą z podanym miesiącem
    """
    wb = Workbook()
    ws = wb.active
    list_of_days = []
    cal1 = calendar.Calendar()

    for day in cal1.itermonthdays2(year, month):
        if day[0] == 0:
            continue
        list_of_days.append(day)

    ws.row_dimensions[1].height = 50

    i = 0
    while i != len(list_of_days):
        ws.cell(column=i + 1, row=2, value=str(datetime.date(year, month, list_of_days[i][0]).day)).alignment = Alignment(
            horizontal='center', vertical='center')
        ws.cell(column=i + 1, row=2).font = Font(size=10)
        if list_of_days[i][1] == 5 or list_of_days[i][1] == 6:
            ws.cell(column=i + 1, row=2).font = Font(color="FF0000", bold=True)
            ws.cell(column=i + 1, row=2).alignment = Alignment(horizontal='center', vertical='center')

        ws.column_dimensions[get_column_letter(i+1)].width = 5
        i += 1
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=len(list_of_days))
    ws.cell(column=1, row=1, value=data.month_list[month - 1]).font = Font(bold=True, size=20)
    ws.cell(column=1, row=1).alignment = Alignment(horizontal='center', vertical='center')

    return wb
