class Employers:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname



    def __str__(self):
        return '{} {}'.format(self.name, self.surname)
