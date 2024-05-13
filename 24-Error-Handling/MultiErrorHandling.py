try:
    x=10
    my_list=[1,2,y]
    z= my_list[3]

except ZeroDivisionError:
    print("You Cannot divide by zero")
except IndexError:
    print("You cannot use an index out of range")
except:
    print("Oh no! something went wrong") 
