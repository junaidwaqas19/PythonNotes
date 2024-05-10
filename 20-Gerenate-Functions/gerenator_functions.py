def gerenator_even_numbers(limit):
    num=0 
    while num<=limit:
        yield num
        num+=2

evens =gerenator_even_numbers(4)
for num in evens:
  print(num)

  # prime numbers display

def generate_prime_numbers():
    primies=[]
    num = 2
    while True:
        if all(num % prime !=0 for prime in primies):
            yield num
            primies.append(num)
        num+=1
prime_generator = generate_prime_numbers()
primes = [next (prime_generator) for i in range(5)]
print(primes)
            
