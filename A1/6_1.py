sumodd = 0
def oddsum(n):
    for i in range(n):
        if (i+1) % 2 != 0:
            sumodd += (i+1)
n = int(input("enter a number: "))
oddsum(n)
print(sumodd)
