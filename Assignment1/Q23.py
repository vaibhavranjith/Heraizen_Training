n=int(input('Enter a number:\n'))
sum=0
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=" ")
        sum+=i
print()
print("The sum the numbers is:"+str(sum))