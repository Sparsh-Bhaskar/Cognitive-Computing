n = int(input("enter a number: "))
sum = 0
for i in range (n):
    if (i+1) % 7 == 0 and (i+1) % 9 == 0:
        sum = sum + (i+1)

print("the sum of numbers divisible by 7 and 9 both is : ", sum)