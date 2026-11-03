class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def add_marks(self, value):
        if value > 0:
            self.__marks += value

    def view_marks(self):
        return self.__marks
s = Student("Aisha", 75)
s.add_marks(10)
print(s.name)
print(s.view_marks())
