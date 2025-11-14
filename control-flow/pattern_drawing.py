x= int (input("Enter the size of the pattern:"))
y = x
while y:
    for i in range(0, x):
        print("*", end="")
    print("")
    y -=1
    