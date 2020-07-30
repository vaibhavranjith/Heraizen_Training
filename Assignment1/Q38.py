l=[[0]*3 for _ in range(3)]
for i in range(3):
    l[i]=[int(i) for i in input().split(" ")]  
big=l[0][0]
small=l[0][0]
for i in range(3):
    for j in range(3):
        if(l[i][j]>big):
            big=l[i][j]
        if(l[i][j]<small):
            small=l[i][j]
print(f"Largest element is {big} and smallest element is {small}")