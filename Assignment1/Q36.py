for i in range(1,5):
    print("@",end="")
print()
for j in range(1,5):
    if(j==1 or j==4):
        print("@",end="")
    else:
        print(" ",end="")
print()
for i in range(1,5):
    print("@",end="")
print()
for i in range(1,3):
    for j in range(1,5):
        if(j==1 or j==4):
            print("@",end="")
        else:
            print(" ",end="")
    print()