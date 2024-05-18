class Dessert:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor

    def cook(self):
        print(f"You bake the {self.flavor} {self.name}")

class Cookie(Dessert):
    def __init__(self, name, flavor, price):
        super().__init__(name, flavor)
        self.price = price
        
    def dunk(self):
        print(f"You dunk the {self.name} in the milk")

    def bake_and_sell(self):
        super().cook()
        print(f"You sell the {self.name} for ${self.price:.2f}")

pie = Dessert("pie", "Cookie")
pie.cook()

cookie = Cookie("cookie", "chocolate chip", 4.99)
cookie.bake_and_sell()
