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

# my_cursor.execute("CREATE TABLE Persons (Id int  AUTO_INCREMENT PRIMARY KEY, name varchar (50) NOT NULL, last_name varchar (50) NOT NULL)")
'''Tworzenie tabeli Persons'''

# sql = "INSERT INTO Persons (id, name, last_name) VALUES (%s, %s, %s)"
# val = (main.add_employer().id, main.add_employer().name, main.add_employer().last_name)
# my_cursor.execute(sql, val)

# sql = "INSERT INTO Persons (name, last_name) VALUES (%s, %s)"
# val = ("Joanna", "Wystemp")
# my_cursor.execute(sql, val)
# employers_db.commit()

# my_cursor.execute("SELECT * FROM Persons")

# my_result = my_cursor.fetchall()
# # print(my_result)

# for x in my_result:
#     print(x[1:])
