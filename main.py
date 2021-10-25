"""
Projekt ma za zadanie pobranie plików wsadowych (czyt. godziny oraz prośby) zaczytanie ich, a następnie
zwrócenie danych w postaci tabeli miesięcznej na zadany rok oraz miesiąc z informacją kto i kiedy ma dyżur, łącznie z
uwzględnieniem dni wolnych, wolnych dni po 24h dyżuru oraz tak żeby obsadzone były wszystkie dni i godziny w
wystarczającej ilości osób.
"""

import XLS
import employers


year = int(input("Podaj rok: "))
month = int(input("Podaj miesiąc: "))
XLS.month_to_csv(year, month)

emp1 = employers.Employers('Jolanta', 'Filipiak')
print(emp1)