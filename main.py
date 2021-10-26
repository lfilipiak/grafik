"""
Projekt ma za zadanie pobranie plików wsadowych (czyt. godziny oraz prośby) zaczytanie ich, a następnie
zwrócenie danych w postaci tabeli miesięcznej na zadany rok oraz miesiąc z informacją kto i kiedy ma dyżur, łącznie z
uwzględnieniem dni wolnych, wolnych dni po 24h dyżuru oraz tak żeby obsadzone były wszystkie dni i godziny w
wystarczającej ilości osób.
"""

import XLS
import employers
from data import file_name
from openpyxl import load_workbook
from openpyxl import formatting

# year = int(input("Podaj rok: "))
# month = int(input("Podaj miesiąc: "))
# XLS.month_to_csv(year, month)
xls = XLS.month_to_csv()

emp1 = employers.Employers('Jolanta', 'Filipiak')
print(emp1)


def open_worbook(path):
    workbook = load_workbook(filename=path)
    print("Worksheet names: {}".format(workbook.sheetnames))
    sheet = workbook.active
    print(sheet)
    print("The title of the Worksheet is: {}".format(sheet.title))


def employer():
    return


xls.save(file_name)

# open_worbook(file_name)
