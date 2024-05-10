def process_data(name,*args,age=0,**kwargs):
     print("proceessing data:",name)
     print("*args:",args)
     print("*age:",age)
     print("**kwargs:",kwargs)

process_data("data 2",1,2,3,age=23,city="lahore")
     