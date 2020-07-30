for i in range(1,13):
    if i<=7:
        print("*",end="")
    else:
        print(" ",end="")
print()
for i in range(1,4):
    for j in range(1,13):
        if((j==7 or j==12)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,13):
        print("*",end="")
print()
for i in range(1,4):
    for j in range(1,13):
        if((j==1 or j==7)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,13):
    if i>=7:
        print("*",end="")
    else:
        print(" ",end="")

