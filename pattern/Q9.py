n=5
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    for j in range(2*i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end="")
    print()
