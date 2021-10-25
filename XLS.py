import calendar
import datetime
from openpyxl import Workbook
from openpyxl.styles import Font

def month_to_csv(year=2021, month=1):
    """
    :param month: pobiera wartość miesiąca od 1 do 12
    :return: zwraca plik z tabelą z podanym miesiącem
    """
    file_name = 'grafik.xls'
    path = r'/home/filip/Pulpit/PythonZ/Projekt - grafik/'
    wb = Workbook()
    ws = wb.active
    xls_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE']
    list = []
    cal1 = calendar.Calendar()
    for day in cal1.itermonthdays2(year, month):
        if day[0] == 0:
            continue
        list.append(day)
    length_of_the_month = len(list)
    i = 0
    while i != length_of_the_month:
        ws['{}1'.format(xls_list[i])] = str(datetime.date(year, month, list[i][0]))
        if list[i][1] == 5 or list[i][1] == 6:
            ws['{}1'.format(xls_list[i])].font = Font(color="FF0000", bold=True)
        i += 1
    wb.save(file_name)
    pass