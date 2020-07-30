def factorial(n):
    fac=1
    while n>=1:
        fac=fac*n
        n-=1
    return fac
sum=0
for i in range(1,8):
    sum+=(1/factorial(i))
print(f"Sum of the terms is {sum}")
