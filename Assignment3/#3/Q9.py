#Q9
tfile=open("D:/python/Assignment3/Q9.txt","r")
cont=tfile.readlines()
lst=[]
for i in cont:
    i=i.replace(".","")
    i=i.replace("\"","")
    lst.append((i.split(" ")))
cd={}
for j in lst[0]:
        if(j in cd):
            cd[j]+=1
        else:
            cd[j]=1
mn=100
mx=0
for i in cd:
    if(cd[i]<mn):
        mn=cd[i]
    if(cd[i]>mx):
        mx=cd[i]
print("MINIMUM")
for i in cd:
    if(cd[i]==mn):
        print(f"{i} : {cd[i]}")
print("MAXIMUM")
for i in cd:
    if(cd[i]==mx):
        print(f"{i} : {cd[i]}")
tfile.close()
