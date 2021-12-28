"""
24h - następny dzień wolny
4 osoby na dobę (2 na rano, 2 na 24h)
soboty i niedziele na 24h
200 - 240h

8-16
8-20
20-8
8-8

"""

import openpyxl
import os
import random
import datetime
import data
import calendar
import database


def hours(year, month):
    wb = openpyxl.load_workbook("{} {}.xlsx".format(year, data.month_list[month - 1]))
    sheet = wb.active
    database.my_cursor.execute("SELECT * FROM Persons")
    workers = len(database.my_cursor.fetchall())
    print(workers)
    day = 1
    while day != int(calendar.monthrange(year, month)[1]+1):

        day += 1

    return wb.save("{} {}.xlsx".format(year, data.month_list[month - 1]))


# sheet.cell(2, 2, value=123)

hours(1990, 1)
