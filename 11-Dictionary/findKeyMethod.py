persons={
    'first_name': "John",
    'last_name':"doe",
    'age':30,
    'state':'Turkey',
    'job':'programmer',
}

# find dictionary keys

print(persons.keys())

# find dictionary values

print(persons.values())

# tuple form get dictionary 

print(persons.items())

# keys found by using for key

for key in persons.keys():
    print(key)

# find values by using for method
for values in persons.values():
    print(values)


for (key,values) in persons.items():
    print(key,values)


# 

my_list=[1,2,3,4,5,6]
my_dict = dict.fromkeys(my_list)
print(my_dict)

# add values
my_dict = dict.fromkeys(my_list,'Hello world')
print(my_dict)

# add empty values
my_dict = dict.fromkeys(my_list,[])
print(my_dict)

# with for method

my_dict = {x: [] for x in my_list}
my_dict[1].append("hi")
print(my_dict)
