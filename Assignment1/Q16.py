num=int(input("Enter any number:\n"))
isPrime=True
for i in range(2,num//2):
    if num%i==0:
        isPrime=False
pont=("is a prime number" if isPrime else "is not a prime number")
print(f"The entered number {num}  {pont}")