import database

class Employers:

    def __init__(self, name, last_name, id):
        self.id = id
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.last_name)

    def add_worker(self):
        sql = "INSERT INTO Persons (id, name, last_name) VALUES (%s, %s, %s)"
        val = (self.id, self.name, self.last_name)
        database.my_cursor.execute(sql, val)
        database.employers_db.commit()
        print(database.my_cursor.rowcount, "record inserted.")
        pass



