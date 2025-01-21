a = {34, 56, 78, 90}
b = {78, 45, 90, 23}

#union of the sets
uni = a.union(b)
print(uni)

#intersection of the sets
inter = a.intersection(b)
print(inter)

#symmetric difference
sd = a.symmetric_difference(b)
print(sd)

#subset and superset
if all(c in b for c in a):
    print("a is the subset of b")
else:
    print("a is not subset of b")

x = int(input("enter a number: "))
if x in a:
    a.remove(x)
    print("number removed")
else:
    print("number not present")

print(a)