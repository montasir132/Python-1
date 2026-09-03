import math
def prime(n):
    if n == 1 or n % 2 == 0:
        return False
    elif n == 2:
        return True
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n % i == 0:
                return False
        return True
n = int(input("enter your number :"))
res = prime(n)
if res == False:
    print(f"{n} it's not a prime number ")
else:
    print(f"{n} it's a prime number ")