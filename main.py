"""
Projekt ma za zadanie pobranie plików wsadowych (czyt. godziny oraz prośby) zaczytanie ich, a następnie
zwrócenie danych w postaci tabeli miesięcznej na zadany rok oraz miesiąc z informacją kto i kiedy ma dyżur, łącznie z
uwzględnieniem dni wolnych, wolnych dni po 24h dyżuru oraz tak żeby obsadzone były wszystkie dni i godziny w
wystarczającej ilości osób.
"""

import XLS
from employers import Employers
from data import month_list, path
import os
import database
#import hours


def add_work_schedule():
    year = int(input("Podaj rok: "))
    month = int(input("Podaj miesiąc: "))
    if not os.path.isfile(path + '{} {}.xlsx'.format(year, month_list[month - 1])):
        XLS.month_to_csv(year=year, month=month).save(
            '{} {}.xlsx'.format(year, month_list[month - 1]))
    else:
        print("taki grafik już istnieje!")
    pass


def add_worker():
    x = input("Podaj imię pracownika: ")
    y = input("Podaj nazwisko pracownika: ")
    worker = Employers(x, y)
    worker.add_worker()
    pass


def delete_worker():
    last_name = input("Podaj nazwisko pracownika do usunięcia: ")
    sql = "DELETE FROM Persons WHERE last_name = %s"
    val = (last_name,)
    database.my_cursor.execute(sql, val)
    database.employers_db.commit()
    print(database.my_cursor.rowcount, "record deleted.")
    pass


def print_workers():
    my_cursor = database.employers_db.cursor()
    my_cursor.execute("SELECT * FROM Persons")
    for x in enumerate(my_cursor.fetchall()):
        print(x[0]+1, x[1][1:])
    pass


# def add_hours():
#     year = int(input("Podaj rok: "))
#     month = int(input("Podaj miesiąc: "))
#     if not os.path.isfile(path + '{} {}.xlsx'.format(year, month_list[month - 1])):
#         raise ValueError("Brak takiego grafiku")
#     else:
#         hours.hours(year=year, month=month)
#     pass


def _list_of_workers():
    list_of_workers = []
    pass


def menu():
    print("1. Utwórz grafik\n2. Dodaj pracownika\n3. Usuń pracownika\n4. Wyświetl listę pracowników")
    choice = int(input())
    match choice:
        case 1:
            add_work_schedule()
        case 2:
            add_worker()
        case 3:
            delete_worker()
        case 4:
            print_workers()
        # case 5:
        #     add_hours()
            pass
    pass


menu()
