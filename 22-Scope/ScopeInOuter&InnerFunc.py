my_global_var=10,
def outer_function():
    my_local_var=25
    print(f"My_local_var: {my_local_var}")
    print(f"My_global_var: {my_global_var}")
    #create inner function inside outer function
    def inner_function():
        my_inner_var =50
        print(f"my_inner_var:  {my_inner_var}")
        print(f"my_local_var:  {my_local_var}")
        print(f"my_global_var: {my_global_var}")
    # call inner function inside outer function
    inner_function()

outer_function()

        