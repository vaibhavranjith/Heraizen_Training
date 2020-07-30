r=int(input("Rows: "))
c=int(input("Cols: "))
lst=[]
for i in range(r):
    lst.append(list(map(int,input().split(" "))))
mx=lst[0][0]
mn=lst[0][0]
for i in range(r):
    for j in range(c):
        if(lst[i][j]>mx):
            mx=lst[i][j]
        if(lst[i][j]<mn):
            mn=lst[i][j]
print(f"Max: {mx}")
print(f"Min: {mn}")
mnc=[]
mxc=[]
for i in range (c):
    mn=lst[0][i]
    mx =lst[0][i]
    for j in range(r):
        if(lst[j][i]>mx):
            mx=lst[j][i]
        if(lst[j][i]<mn):
            mn=lst[j][i]
    mnc.append(mn)
    mxc.append(mx)
print(f"Col wise min:{mnc}")
print(f"Col wise max:{mxc}")
mxr=[]
mnr=[]
for i in lst:
    mnr.append(min(i))
    mxr.append(max(i))
print(f"Row wise min:{mnr}")
print(f"Row wise max:{mxr}") 