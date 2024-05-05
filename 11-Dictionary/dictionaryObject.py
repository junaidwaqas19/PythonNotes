persons ={
    "first_name": "John",
    "last_name":"doe",
    "age":30,

}

print(persons['first_name'])

# dictaonery key value change

persons["first_name"]='Johan'
print(persons)

# get method to find key from object
print(persons.get('age'))

# result if key not exist

print(persons.get('jobs'))

# key not find message
print(persons.get('jobs','No found jobs'))

# add new record with setDefualt

result = persons.setdefault('job','Programmer')

# display new item of dictionary 
print(result)

# display dictionary of 
print(persons)

# using update method 

persons.update(state='Pakistan')
print(persons)
# using array in updated method

persons.update([['state','Turkey'],['job','Coder']])