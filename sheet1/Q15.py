p = int(input("Enter percentage: "))

if p < 25:
    print("D")
elif p <= 45:
    print("C")
elif p <= 65:
    print("B")
elif p <= 85:
    print("A")
else:
    print("A+")
