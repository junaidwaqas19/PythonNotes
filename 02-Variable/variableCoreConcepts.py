# current value show
x=5
x='seven'
print(x)

# simultaneous assignments string
a,b,c= "apple","banana","coconut"
print(a,b,c)

# Multiple Assignments
a = b = c = 0
print("Multiple Assignments - a:", a, "b:", b, "c:", c)

# Simultaneous Assignments Numbers
x, y = 5, 10
print("Simultaneous Assignments - x:", x, "y:", y)

# Unpacking Assignments
x, *y, z = 1, 2, 3, 4, 5
print("Unpacking Assignments - x:", x, "y:", y, "z:", z)

# Augmented Assignments
x = 5
x += 3  # Equivalent to x = x + 3
print("Augmented Assignments - x:", x)