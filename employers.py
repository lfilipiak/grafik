import database


class Employers:

    list_of_workers = {}

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def str(self):
        pass

    def add_worker(self):
        # database.my_cursor.execute("SELECT * FROM Persons")
        sql = "INSERT INTO Persons (name, last_name) VALUES (%s, %s)"
        val = (self.name, self.last_name)
        database.my_cursor.execute(sql, val)
        database.employers_db.commit()
        print(database.my_cursor.rowcount, "record inserted.")
        pass

    def delete_worker(self):
        database.my_cursor.execute("DELETE FROM Persons WHERE last_name={}".format(self.last_name))
        database.employers_db.commit()
        print(database.my_cursor.rowcount, "record deleted.")
        pass

    def _list_of_workers(self):
        pass


