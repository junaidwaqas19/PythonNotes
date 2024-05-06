# using with opreator
str_one = "Helo"
str_two ="Helo"

result = str_one is str_two

print(result)

# with id opreator 

result =id(str_one)
print(result)

# display both 

print(result,id(str_two))

# with array 

str_arr_one =[1,2,3]
str_arr_two =[1,2,3]

result = str_arr_one is not str_arr_two
print(result)
# using thire list

list_third =str_arr_one
result = str_arr_one is  list_third

print(result)