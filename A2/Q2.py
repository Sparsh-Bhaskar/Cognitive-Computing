t = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

#give max and its index
m = max(t)
i = t.index(m)
print (f"the largest value is {m} and the index is {i}")

#give the min and its frequency
n = min(t)
count = 0
for c in t:
    if c == n:
        count += 1
print(f"the smallest value is {n} and it occurs {count} times")

#reverse the tuple and return it as a list
l = list(t)
l.reverse()
print(l)

#check if user input is present in the tuple or not
x = int(input("enter the number to check : "))
if x in t:
    print(f"{x} is present in the tuple at index {t.index(x)}")
else:
    print("the number is not present")