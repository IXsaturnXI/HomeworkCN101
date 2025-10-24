print("2. Pyramid of *")
Rows = int(input("Enter number of rows to show Pyramid: "))
print("2.1")
for i in range(1 , Rows+1):
    for j in range(Rows - i):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")
    print()
print("2.2")
for i in range(1 , Rows+1):
    for j in range(Rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


