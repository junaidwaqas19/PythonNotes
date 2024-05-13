my_global_var =10
def modify_global():
    print(f"my_global_var : {my_global_var}")

modify_global()

# using global keyword to declare global variable

def modify_globals():
    global  my_global_var
    my_global_var =20

modify_globals()    
print(f"my_global_var : {my_global_var}")
# display dictionary with global variables
print(globals().keys())
