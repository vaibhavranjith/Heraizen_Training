#Q5
x=list(map(int,input("Enter array x: ").split(" ")))
y=list(map(int,input("Enter array y: ").split(" ")))
z=list(map(lambda n1,n2: n1+n2,x,y))
print(z)