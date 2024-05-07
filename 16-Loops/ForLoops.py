animals =['cat','dogs','hen']

for animal in animals:
    if animal == 'dogs':
       print(animal)
       break
       
# using loop with range

for i in range(len(animals)):
    animals[i] = 'goat'
    print(animals[i])
print(animals)

# with string chracter

for char in "welcome in python":
    print(char)

    