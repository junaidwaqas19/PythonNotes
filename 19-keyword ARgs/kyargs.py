# kwargs empty 
def print_details(**kwargs):
      print(f"kwargs:{kwargs}")
      for key, value in kwargs.items():
         print(f"{key}:{value}")


print_details(name="Abdullah",age=23,city="Lahore")


