import mysql.connector

employers_db = mysql.connector.connect(
    host='localhost',
    user='filip',
    password='lucas16',
    database='Workers'
)

my_cursor = employers_db.cursor()

# my_cursor.execute("CREATE DATABASE Workers")
'''Tworzenie bazy danych Workers'''

# my_cursor.execute("CREATE TABLE Persons (Id int(10) NOT NULL, name varchar(10), last_name varchar(10))")
'''Tworzenie tabeli Persons'''

# sql = "INSERT INTO Persons (id, name, last_name) VALUES (%s, %s, %s)"
# val = (main.add_employer().id, main.add_employer().name, main.add_employer().last_name)
# my_cursor.execute(sql, val)

my_cursor.execute("SELECT * FROM Persons")

my_result = my_cursor.fetchall()
print(my_result)

# for x in myresult:
#     print(x[2])
