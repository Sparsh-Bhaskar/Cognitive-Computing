import math
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m = int(input("enter a number: "))
sum = 0

for i in range (m):
    if(isprime(i+1)):
        sum += (i+1)

print(f"sum of prime numbers till {m} is: ", sum)