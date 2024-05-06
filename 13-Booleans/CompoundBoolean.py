a=5
b=10
c=25
d=10

# with and opreator 
result = a < b and b<c
print(result)

# with or opreator 
result = a < b or b<c
print(result)

# combined and or opreator use

result = (a<b) and (b>a) or (a==5)
print(result)

# combined and or opreator use witn not 

result =not (a<b and b>a) or a==5
print(result)
