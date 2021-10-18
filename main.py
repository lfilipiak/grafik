"""
Projekt ma za zadanie pobranie plików wsadowych (czyt. godziny oraz prośby) zaczytanie ich, a następnie
zwrócenie danych w postaci tabeli miesięcznej na zadany rok oraz miesiąc z informacją kto i kiedy ma dyżur, łącznie z
uwzględnieniem dni wolnych, wolnych dni po 24h dyżuru oraz tak żeby obsadzone były wszystkie dni i godziny w
wystarczającej ilości osób.
"""

import datetime as dt
import os

import openpyxl
import openpyxl as opxl
import pandas as pd


def month_to_csv(month):
    """
    :param month: pobiera wartość miesiąca od 1 do 12
    :return: zwraca plik z tabelą z podanym miesiącem
    """
    file_name = 'grafik.xls'
    df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]], index=['jeden', 'dwa', 'trzy'],
                      columns=['a', 'b', 'c'])
    path = r'/home/filip/Pulpit/PythonZ/Projekt - grafik/'
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.get_sheet_by_name("spam")
    sheet.title = "df data"
    wb.save('save.xls')

    xlr = pd.ExcelWriter('save.xls')
    df.

        # file.write(str(dt.datetime(year=2021, month=month, day=12)))

    return


month_to_csv(1)
