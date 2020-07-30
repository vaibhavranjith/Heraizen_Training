n=int(input('Enter a number:\n'))
sum=n
while sum>9:
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    n=sum
print(f"The single digit sum is {sum}")