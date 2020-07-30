n=int(input("Enter any number:\n"))
sum=0
while n>0:
    sum+=n%10
    n=n//10
    sum*=10
sum=sum//10
print(f"The number reversed is {sum}")