n=int(input("Enter the number of rows:\n"))
c=1
for i in range(1,n+1):
    for j in range(1,4):
        print(c,end=" ")
        c+=1
    print()