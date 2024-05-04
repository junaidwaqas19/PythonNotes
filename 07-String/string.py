# string declaration with double qoutes
string_data="this store string"
print(string_data)
# combined two string
greeting ="Hi!,"
questions="How are you"
message = greeting +" "+questions
print (message) 

#string with assignment opreator

laugh ="ha"
laugh*=3
print(laugh)

# string with multi line

multi_line ="""This is multi line 
 String you see in
 output"""
print(multi_line)

# string length function 

password = "check1234"
psw_length = len(password)
print(psw_length)

# string chracter

name="Abdullah Rizwan"
print(name[0])

# Find Range of chracter from string words with single colon sign
print(name[0:9])

# without using first range
print(name[:9])
# without declare last range
print(name[8:])