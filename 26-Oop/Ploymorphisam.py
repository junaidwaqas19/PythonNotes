class Food:
    def __init__(self, name):
        self.name = name

    def is_delicious(self):
        return False

class Fruit(Food):
    def is_delicious(self):
        return True

class Vegetable(Food):
    def is_delicious(self):
        return False

# Function that checks if food is delicious
def check_deliciousness(food):
    if food.is_delicious():
        print(f"{food.name} is delicious!")
    else:
        print(f"{food.name} is not delicious.")

# Creating instances of fruits and vegetables
apple = Fruit("Apple")
banana = Fruit("Banana")
carrot = Vegetable("Carrot")
broccoli = Vegetable("Broccoli")

# Checking deliciousness of each food
check_deliciousness(apple)      # Output: Apple is delicious!
check_deliciousness(banana)     # Output: Banana is delicious!
check_deliciousness(carrot)     # Output: Carrot is not delicious.
check_deliciousness(broccoli)   # Output: Broccoli is not delicious.
