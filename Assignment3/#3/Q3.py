#Q3
tfile=open("D:/python/Assignment3/Q3.txt","r")
cont=tfile.readlines()
tt=[]
fmt="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
print(fmt.format(*list(cont[0].split(","))))
for i in range(1,len(cont)):
    tt.append(list(map(int,cont[i].replace("\n","").split(","))))
query=input("Enter the day: ")
opt={"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
sum=0
print(f"The working hours: {tt[0][opt[query]]+tt[1][opt[query]]+tt[2][opt[query]] }")
tfile.close()