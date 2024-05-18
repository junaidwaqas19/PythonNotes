class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        return f"A {self.color} {self.make} {self.model} Made in {self.year}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Car):
            return (
                self.color == other.color and
                self.make == other.make and
                self.model == other.model and
                self.year == other.year
            )
        return False

car1 =Car("black","chevy","silverodi",2023)
car2 =Car("black","Kia","silverodi",2024) 
car3 =Car("black","chevy","silverodi",2023)
print(car1==car2)
print(car1==car3)

num=2
