# Invalid variable declarations
2nd_variable = "Invalid"  # Starts with a number
my-variable = 10         # Contains a special character (-)
for = 5                   # Same as Python keyword 'for'
if = True                # Same as Python keyword 'if'

# Attempting to print variables with invalid names will result in errors
print(2nd_variable)  # Error: SyntaxError: can't assign to literal
print(my-variable)   # Error: SyntaxError: can't assign to operator
print(for)           # Error: SyntaxError: invalid syntax
print(if)            # Error: SyntaxError: invalid syntax
