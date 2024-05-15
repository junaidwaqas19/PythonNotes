class Counter:
    count =0
    def __init__(self,name):
        self.name=name
        Counter.count +=1

Counter1 = Counter("one")
print(f"Counter {Counter1.name} count: {Counter1.count}" )
Counter2 = Counter("Two")

print(f"Counter {Counter2.name} count: {Counter2.count}" )

