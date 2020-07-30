#Q10
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
print(f"Total number of unique words: {len(cd)}")