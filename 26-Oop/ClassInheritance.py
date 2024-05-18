class Dessert:
    def __init__(self, name, flavor):
        self.name = name
        self.flavor = flavor

    def cook(self):
        print(f"You bake the {self.flavor} {self.name}")

class Cookie(Dessert):
    def __init__(self,name,flavor,price):
             Dessert.__init__(self,name,flavor)
             self.price = price
        
    def dunk(self):
        print(f"You dunk the {self.name} in the milk")

pie = Dessert("pie", "Cookie")
pie.cook()

cookie = Cookie("cookie", "chocolatechip",4.99)
#  pie.cook()
#  cookie.cook()
#  cookie.dunk()
#  pie.dunk()

print(cookie.price)