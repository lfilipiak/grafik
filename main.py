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


def add_work_schedule():
    year = int(input("Podaj rok: "))
    month = int(input("Podaj miesiąc: "))
    if not os.path.isfile(path + '{} {}.xlsx'.format(year, month_list[month - 1])):
        XLS.month_to_csv(year=year, month=month).save('{} {}.xlsx'.format(year, month_list[month - 1]))
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


def _list_of_workers():
    list_of_workers = []

    pass


# def delete_worker():
#     x = input("Podaj nazwisko pracownika do usunięcia: ")


def menu():
    print("1. Utwórz grafik\n2. Dodaj pracownika\n3. Edytuj grafik")
    choice = int(input())
    match choice:
        case 1:
            add_work_schedule()
        case 2:
            add_worker()
        case 3:
            pass
    pass



delete_worker()
# print("WYBIERZ FUNKCJĘ:")
# menu()
