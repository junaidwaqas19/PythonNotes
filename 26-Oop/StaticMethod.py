class Mathutiliy:
    
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
    @staticmethod
    def square(a):
        return a**2
add     = Mathutiliy.add(2,3)
sub     = Mathutiliy.sub(2,4)
square  = Mathutiliy.square(2)

print(f"Add: {add} Sub: {sub} Square: {square}")