#set with none 
my_set =None
print(my_set)

# set value
my_set = {1,2,3}
print(my_set)

# set unique value
my_set = {1,2,3,2,3}
print(my_set)

# set with empty show dicioneries

my_empty_set ={}
print(my_empty_set)
print(type(my_empty_set))

# set value By set function
set_fun = set([1,2,3])
print(set_fun)

# find string in set
my_set = {l for l in "abacadabacdabcabc" if l in'abc' }
print(my_set)