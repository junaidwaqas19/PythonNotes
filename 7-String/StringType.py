my_string = "welcome in python"

# string captial method

print(my_string.capitalize())
#--> can use directly
print("this is string".capitalize())
# string casefold method for lower case 
my_string_low ="WELCOME IN PYTHON"
print(my_string_low.casefold())

# string count
string_count = "abababababa"
print(string_count.count("aba"))
#--> with start
print(string_count.count("aba",4))
#--> for end
print(string_count.count("aba",4,7))

# string Find method

string_find = "you know you can do it"
#--> String by words
print('String Find:',string_find.find('you'))
# --> string by number parameters

print('String Find Through Number:',string_find.find('you',1))
#--> string not found output
print('String Not Found Through Number:',string_find.find('z'))

#--> stirng find through in opreator
print('you' in string_find)