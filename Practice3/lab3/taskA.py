def valid(n):
    while n > 0:
        v1 = n % 10
        if v1 % 2 != 0:
            return False
        n //= 10
    return True
n = int(input())

if valid(n):
    print("Valid")
else:
    print("Not valid")

