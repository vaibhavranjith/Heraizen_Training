def op1(lst):
    qual=input("Enter the required qualifiction: ")
    c=0
    for st in lst:
        if(st[4]==qual):
            print(*st)
            c+=1
    if(c==0):
        print("No student with the given qualification")

def op2(data):
    count={}
    for val in data:
        if(val[4] in count):
            count[val[4]]+=1
        else :
            count[val[4]]=1
    for i in count:
        print(f"The number of students in {i}: {count[i]}")

def op3(data):
    count=0
    for val in data:
        if(val[3]=='Y'):
            count+=1
    print(f"The total number of students placed: {count}")

def op4(data):
    count=0
    for i in data:
        if(i[2]=='Y' and i[3]=='N'):
            count+=1
    print(f"The number of student that completed but whod did'nt get placed: {count}")

def op5(data):
    cty=0
    ctn=0
    for val in data:
        if(val[3]=='Y'):
            cty+=1
        else:
            ctn+=1
    print(f"The number of students placed: {cty}")
    print(f"The number of students not placed: {ctn} ")

def op6(data):
    count=True
    name=input("Enter the name to search: ")
    for val in data:
        if(name.casefold()==val[0].casefold()):
            print(*val)
            count=False
    if(count):
        print('No Records Found')
def op7(data):
    cty=0
    ctn=0
    for val in data:
        if(val[3]=='Y'):
            cty+=1
        else:
            ctn+=1
    print(f"Placement success: {(cty*100)/(cty+ctn)}")

def op8(data):
    max=0.0
    for i in data:
        if i[5]>max:
            max=i[5]
    print("The student(s) with highest score: ")
    for i in data:
        if i[5]==max:
            print(*i)
def op9(data):
    print("The students names: ")
    for i in data:
        print(i[0])
def op10(data):
    print("The student name Qualifications are:")
    for i in data:
        print(f"{i[0]} {i[4]} {i[5]}")

def call_func(data,f):
    f(data)
    
qfile=open("D:/python/Assignment3/#2/coursedata.csv","r")
cont=qfile.readlines()
data=[]
for i in range(1,len(cont)):
    lst=list(cont[i].split(","))
    lst[5]=float(lst[5].replace("\n",""))
    data.append(lst)
print("1. Get all students by the given qualification")
print("2. Get count of all the students by qualification")
print("3. Get count of students who got placed")
print("4. Get count of student who completed course but not placed")	
print("5. Get count of placed and not placed student")
print("6. Search student by the given name")	
print("7. Get average success rate of the given batch")	
print("8. Get max percentage scored Student details")
print("9. Get all the student name only")
print("10.Get all the student name,qualification,score")
print("-"*50) 
opt=int(input("Enter an query[1-10]: "))
call_list={1:op1 , 2:op2 ,3:op3,4:op4,5:op5,6:op6,7:op7,8:op9,10:op10}
call_func(data,call_list[opt])

qfile.close()