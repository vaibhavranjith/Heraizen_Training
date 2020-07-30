n=int(input("Enter the number:\n"))
print("Output")
new=0
i=4
while i>=0:
    dig=n//(10**i)
    if(dig==9):
        new+=9*(10**i)
    else:
        new+=(dig+1)*(10**i)
    n=n%(10**i)
    i-=1
print(new)
    
    