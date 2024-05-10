
# display list values 
def calculate_sum(*args):
    return args

result = calculate_sum(1,2,3)
print(result)

# using with loop and sum 
def calculate_sum(*args):
    total =0
    for num in args:
        total+=num
    return total

result = calculate_sum(1,2,3)
print(result)

# with builtin sum functin
def calculate_sum(*args):
    return sum(args)

result = calculate_sum(1,2,3)
print(result)

