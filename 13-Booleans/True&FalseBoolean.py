# The and operator has higher precedence than the or operator. So, the expression is evaluated from left to right.
# not False evaluates to True.
# True and True evaluates to True.
# True or True evaluates to True.
result = True or False and not False

# So, the value of result would be True. When you print result
print(result)
