n=int(input("Enter a number:\n"))
sum=0
for i in range(1,n+1):
    sum+=(1/i**3)
print("The sum of the series is "+str(sum))
