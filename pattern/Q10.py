n=5
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    for j in range(2*(n-1-i)):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()
