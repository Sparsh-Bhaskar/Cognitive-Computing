n = int(input("enter the number which u want a table of: "))

print(f"\n--the table of {n}--\n")
for i in range (10):
    print(f"{n} * {i+1} = ", (n*(i+1)))