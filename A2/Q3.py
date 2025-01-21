import random
import math

l = []
even = []
odd = []
prime = []

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        

for i in range(0,100):
    x = random.randint(100,900)
    l.append(x)

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
    
    if(isprime(i)):
        prime.append(i)
    

print("even count:", len(even))
print(even)
print("odd count: ", len(odd))
print(odd)
print("prime count is: ",len(prime))
print(prime)

