a = int(input())
rev = 0
n = a
while n > 0:
    rev = rev*10 + n%10
    n //= 10
if rev == a:
    print("Yes")
else:
    print("No")
