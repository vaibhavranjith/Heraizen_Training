n=int(input("enter a number: "))
s=0
product=1
while n>0:
    dig=n%10
    s+=dig
    if(dig!=0):
        product=product*dig
    n=n//10
print(s)
print(product)
