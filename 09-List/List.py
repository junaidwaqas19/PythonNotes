# empty_list
my_list =None
print(my_list)

# with value list
my_list= ['Goat','Lion']
print(my_list)

#with list function
my_list =list()
print(my_list)
#--> List Function With Value

my_list=(list('Hen'))
print(my_list)

# using append to add new value into list

my_list=['hen','goat']
my_list.append(1)
print(my_list)

#using append to add string to list
my_list=['hen','goat']
my_list.append('cow')
print(my_list)

#using insert method to add value on desired index

my_list.insert(1,'duck')
print(my_list)
# Extend or merge two lists
my_other_list=['horse','pegion']
my_list.extend(my_other_list)
print(my_list)

#print list specfic values
my_list=['hen','duck','cow','horse','pegion']
print(my_list[2])

#list specfic items display with negative index

print(my_list[-1])
print(my_list[-5])
#list value change

my_list[4]='donkey'
print(my_list)

# using single colon : to display range of list items

print(my_list[0:3])

#using range sequence like mathmatic terms sequnce using here
print(my_list[0:5:2])

# list length 
print(len(my_list))

