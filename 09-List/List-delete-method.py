
# remove item from list
my_list=['hen','duck','cow','horse','pegion','cow']
print(my_list.remove('cow'))
print('Remove Method:',my_list)

# using delete method 

my_list=['hen','duck','cow','horse','pegion','cow']
del my_list[2]
print('Deleted Method:',my_list)

#using pop method
my_list=['hen','duck','cow','horse','pegion','cow']

print(my_list.pop())
print('Pop Method',my_list) 

#using clear method to list empty
my_list=['hen','duck','cow','horse','pegion','cow']

print(my_list.clear())
print('Clear Method:',my_list)