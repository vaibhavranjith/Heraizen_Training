n=int(input("Enter the number of rows:\n"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==i):
            print(19,end=" ")
        else:
            print(0,end=" ")
    print()