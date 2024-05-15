# class declare
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.weight="unknown"
    def Student(self):
        print(f"{self.name } is student")
persone1 = Person('Abudllah',4)
persone2 = Person('Mohaid',7)
print(f"{persone1.name} is {persone1.age} years old")
print(f"{persone2.name} is {persone2.age} years old")

persone1.Student()


    