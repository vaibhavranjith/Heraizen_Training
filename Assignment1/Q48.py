n=int(input("Enter the number:\n"))
print("Output")
i=3
temp=n
while i>=0:
    print(f"{n//(10**i)}*{10**i}={(n//(10**i))*10**i} ")
    n=temp%(10**i)
    i-=1