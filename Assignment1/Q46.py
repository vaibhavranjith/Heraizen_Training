def isPrime(n):
    if(n==1):
        return False
    for i in range(2,(n+1)//2):
        if n%i==0:
           return False
    return True

n=int(input('Enter the number\n')) 
c=0
while n>0:
    if(isPrime(n%10)):
        c+=1
    n//=10
print(f"Number of prime digits is {c}")