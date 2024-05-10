numbers =[1,2,3,4,5,6]
squared_numbers =list(map(lambda x:x**2,numbers))
print(squared_numbers)

# for even

even_numbers = list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

students = [('Alice',25),('James',20),('Mark',26)]
students.sort(key = lambda x:x[1]) # sort by age 
print(students)

# complex Funtion 

def apply_opreations(x,y,opreations=lambda a,b:a+b):
    return opreations(x,y)

multiply = lambda a,b:a*b
add  = apply_opreations(5,3)
multi = apply_opreations(7,8,multiply)

print (add)
print (multi)
