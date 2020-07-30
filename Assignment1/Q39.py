#n=int(input("Enter the number of rows:\n"))
n=5
for i in range(1,6):
    for j in range(n+2-i,n+1):
        print(j,end=" ")
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()