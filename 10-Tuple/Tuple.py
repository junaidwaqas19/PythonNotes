
#  tuple
numbers = ()
print(type(numbers))

#  tuple
numbers=(1)
print(type(numbers))

# with comma
numbers=(1,)
print(type(numbers))

# find tuple lengths 

numbers=len((1,2,3))
print(numbers)
# declare tuple with tuple keywords

numbers = tuple([1,2,3])
print(numbers)
# specfic item display from tuple

my_tuple = tuple([1,3.14,"Hi"])
print(my_tuple[0:3:2])

#tuple value assign to variable
my_other_tuple = tuple([1,2,3])
a,b,c=my_other_tuple #assign tuple value to variable
print(a,b,c) # display tuple value through variables

# join two tuples

conc_tuple = my_other_tuple + my_tuple
print(conc_tuple)

# count method use in tuple
count_tuple =(1,2,3,1,3.14,"Hi")
print(count_tuple.count(1)) # count specfic value in tuple 

# tuple index find

print(count_tuple.index(2,1,4))