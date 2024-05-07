counter =0
# while counter <= 5:
#     print(counter)
#     counter += 1

# using with if condition

while counter <= 5:
    if counter %2 ==0:
        print(counter)
        counter+=1
        continue
    counter += 1
else:
    print("done")

while True:
    print("hi")
    if input("Enter q to exit:") == 'q':
        break
    
