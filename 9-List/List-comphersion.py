numbers=[1,2,3,4,5,6]
new_list =[num ** 2 for num in numbers]
print(new_list)

# example 2
numbers=[1,2,3,4,5,6]
new_list =[num ** 2 for num in numbers if num% 2==0]
print(new_list)

# list create with conditions 
num = [0]*10
print(num)
 # add my value to my list
num[2] =4  
print(num)