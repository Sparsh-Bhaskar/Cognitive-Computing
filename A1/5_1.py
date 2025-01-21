nums = []

print("enter 3 numbers\n")
for i in range (3):
    num = int(input("enter no. "))
    nums.append(num)

h = max(nums)

print("the largest number is: ", h)