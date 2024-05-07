
# when write only one value in range 
#than it take as end value and 
#by defualt 0 start value
my_range =range(4)
print(my_range)

# using list to display range all value
print(list(my_range))

# display range with start and end values

print(list(range(4,10)))

# only even number 

print(list(range(4,10,2)))

# find the length of range

print(len(range(4,12)))

# sum of range 
print(sum(range(4,12)))
# using loop

for i in range(10):
    print(i)