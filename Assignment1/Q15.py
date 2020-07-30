num=int(input("Enter the number of natural numbers to be generated:\n"))
print(f"First {num} natural numbers are: ",end="")
for i in range(1,num+1):
    print(str(i)+" ",end="")
    