my_set1 ={1,2,3,4}
my_set2 ={3,4,5,6}
my_set3 ={1,2,3,4,5}
my_set4 ={5,6,7,8}

result = my_set1.difference(my_set2)

print(result)

#alternative set difference method

result = my_set1 - my_set2
print(result)

# set intersection method

result = my_set1.intersection(my_set2)
print(result)

# set union

result= my_set1.union(my_set2)
print(result)

# conditional opreator

result = my_set1 | my_set2
print(result)

# symestric set

result = my_set1 ^ my_set2
print(result)

# differnt update method 

result = my_set1.difference(my_set2)

print(result)

# symmertic_differece
result = my_set1.symmetric_difference(my_set2)
print(result)

# with symbole

my_set1 -= my_set2
print(my_set1)

# boolean apply

result = my_set1.isdisjoint(my_set4)
print(result)
#superset method
result = my_set1.issuperset(my_set4)
print(result)

#isubset 
result = my_set1.issubset(my_set3)
print(result)
