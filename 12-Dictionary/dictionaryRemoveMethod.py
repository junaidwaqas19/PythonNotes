persons={
    'first_name': "John",
    'last_name':"doe",
    'age':30,
    'state':'Turkey',
    'job':'programmer',
}

# pop method
result =persons.pop('job')

print(result)
print(persons)

# pop item method to delete last method
result =persons.popitem()

print(result)
print(persons)

# using del method to deletekey

del persons['age']
print(persons)

# dictionary all record delete

persons.clear()
print(persons)
