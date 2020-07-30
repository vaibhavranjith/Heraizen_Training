r=int(input("Enter the number of rows: \n"))
c=1
p=1
for i in range(0,r+1):
    for j in range(c,2**i):
        print(j,end=" ")
        c+=1
    print()
 