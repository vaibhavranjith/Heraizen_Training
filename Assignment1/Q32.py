n=int(input("Enter the number of rows:\n"))
count=ord('A')
for i in range(1,n+1):
    for j in range(1,4):
        print(chr(count),end=" ")
        count+=1
    print()