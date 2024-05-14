with open('example.txt', 'a') as file:
    file.write('\nwrite python code')
    file.flush()  # Flush the buffer to ensure immediate writing



# find file
# try:
#     with open("non_existent_file.txt",'r') as file:
#         data = file.read()

# except FileNotFoundError:
#     print("File not found!")

# write code in file
# try:
#     with open('example.txt','x') as file:
#         file.write("welcome in python")
       

# except:
#     print("File already exists")

