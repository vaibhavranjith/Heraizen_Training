n=int(input('Enter a number:'))
sum=0
temp=n
while n>0:
    sum+=(n%10)**3
    n=n//10
if(temp==sum):
    print("THe number is an amstrong number")
else:
    print("The number is not an amstrong number")
