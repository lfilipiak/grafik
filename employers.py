import database


class Employers:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def str(self):
        pass

    def add_worker(self):
        database.my_cursor.execute("SELECT * FROM Persons")
        sql = "INSERT INTO Persons (id, name, last_name) VALUES (%s, %s, %s)"
        val = (database.my_cursor.fetchall()[-1][0] + 1, self.name, self.last_name)
        database.my_cursor.execute(sql, val)
        database.employers_db.commit()
        print(database.my_cursor.rowcount, "record inserted.")
        pass
