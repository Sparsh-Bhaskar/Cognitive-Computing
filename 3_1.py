# taking input from user

l = []

print("enter 5 names ")
for i in range (5):
    n = input(f"enter name {i+1}: ")
    l.append(n)

print("the list of names is:", l)