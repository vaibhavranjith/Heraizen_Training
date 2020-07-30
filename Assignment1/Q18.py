def isPrime(n):
    for i in range(2,(n+1)//2):
        if n%i==0:
            return False
    return True
lb=int(input("Enter the lower bound:\n"))
ub=int(input("Enter the uppr bound:\n"))
print("The prime numbers between lb and ub are: ")
for i in range(lb,ub+1):
    if(isPrime(i)):
        print(i,end=" ")

    

