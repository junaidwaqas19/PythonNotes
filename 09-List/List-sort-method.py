# Sorting method
animals = ['hen', 'duck', 'cow', 'horse', 'pegion', 'cow']
animals.sort()
print(animals)

# Sorting by length of words
animals = ['hen', 'duck', 'cow', 'horse', 'pegion', 'cow']
animals.sort(key=len)
print(animals)

# Using with reverse method
animals = ['hen', 'duck', 'cow', 'horse', 'pegion', 'cow']
animals.sort(key=len, reverse=True)
print(animals)

# Using sorted() method
animals = ['hen', 'duck', 'cow', 'horse', 'pegion', 'cow']
sorted_animals = sorted(animals)
print(sorted_animals)

# Sorted with key and reverse method
animals = ['hen', 'duck', 'cow', 'horse', 'pegion', 'cow']
result = sorted(animals, key=len, reverse=True)
print(result)

# Sorting characters of a string
result = sorted("hello, worlds")
print(result)
