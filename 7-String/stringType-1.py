space_string ="            Too Many Space          "

# remove spaces
print(space_string.strip())

# dash remove from  String  left side

dash_string = "---------Too many Dashes---------"
print(dash_string.lstrip('-'))

# dash remove from  String  right side

dash_string = "---------Too many Dashes---------"
print(dash_string.rstrip('-'))

#symbol string

symbol_string ="^*-^^*-^#Lots Of symbols^*-^^*-^#"
print(symbol_string.strip('^*-'))

# start String 

qoutes="It is not a bug,it is a feature"
print(qoutes.startswith('It'))

# end String
print(qoutes.endswith('It'))

#replace string

print(qoutes.replace(' ','-'))

# with parameter replace

print(qoutes.replace(' ','-',3))

# with split method

print(qoutes.split('is'))

# string method combined use

print(dash_string.strip('-').upper().split())

# using with join string
join_string = dash_string.strip('-').upper().split()
print('--'.join(join_string))


