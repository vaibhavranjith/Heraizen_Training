from stud import Student

def op1(data):
    header="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
    qual=input("Enter the required qualifiction: ")
    c=0
    print("_"*90)
    print(header.format("Name","Batch","Completed","Placed","Qulaification","Score"))
    print("_"*90)
    for st in data:
        if(st.qual==qual):
            print("-"*90)
            print(header.format(st.name,st.batch,st.cc,st.pc,st.qual,st.score))
            c+=1
    print("_"*90)
    if(c==0):
        print("No student with the given qualification")

def op2(data):
    count={}
    for val in data:
        if(val.qual in count):
            count[val.qual]+=1
        else :
            count[val.qual]=1
    header="{:<15}{:>15}"
    print("_"*90)
    print(header.format("Qualification","Count"))
    print("_"*90)
    for i in count:
        print("-"*90)
        print(header.format(i,count[i]))
    print("_"*90)

def op3(data):
    count=0
    for val in data:
        if(val.pc=='Y'):
            count+=1
    print(f"The total number of students placed: {count}")

def op4(data):
    count=0
    for i in data:
        if(i.cc=='Y' and i.pc=='N'):
            count+=1
    print(f"The number of student that completed but whod did'nt get placed: {count}")
def op5(data):
    cty=0
    ctn=0
    for val in data:
        if(val.pc=='Y'):
            cty+=1
        else:
            ctn+=1
    print(f"The number of students placed:     {cty}")
    print(f"The number of students not placed: {ctn} ")

def op6(data):
    header="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
    count=True
    name=input("Enter the name to search: ")
    print("_"*90)
    print(header.format("Name","Batch","Completed","Placed","Qulaification","Score"))
    print("_"*90)
    for val in data:
        if(name.casefold()==val.name.casefold()):
            print("-"*90)
            print(header.format(val.name,val.batch,val.cc,val.pc,val.qual,val.score))
            count=False
    if(count):
        print('No Records Found')
    print("_"*90)
def op7(data):
    cty=0
    ctn=0
    for val in data:
        if(val.cc=='Y'):
            cty+=1
        else:
            ctn+=1
    print(f"Placement success: {round((cty*100)/(cty+ctn),2)}%")
def op8(data):
    header="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
    max=0.0
    for i in data:
        if i.score>max:
            max=i.score
    print("The student(s) with highest score: ")
    print("_"*90)
    print(header.format("Name","Batch","Completed","Placed","Qulaification","Score"))
    print("_"*90)
    for st in data:
        if st.score==max:
            print("-"*90)
            print(header.format(st.name,st.batch,st.cc,st.pc,st.qual,st.score))
    print("_"*90)
    
def op9(data):
    print("The students names: ")
    print("_"*15)
    for i in data:
        print("-"*15)
        print("{:^15}".format(i.name))
    print("_"*15)

def op10(data):
    header="{:<15}{:<15}{:<15}"
    print("_"*50)
    print(header.format("Name","Qulaification","Score"))
    print("_"*50)
    for i in data:
        print("-"*50)
        print(header.format(i.name ,i.qual, i.score))
    print("_"*50)
    
def call_func(f,data):
    f(data)

qfile=open("D:/python/Assignment3/#2/coursedata.csv","r")
cont=qfile.readlines()
data=[]
entry=Student()
lst=[]
for i in range(1,len(cont)):
    lst=list(cont[i].replace("\n","").split(","))
    entry=Student(lst[0],lst[1],lst[2],lst[3],lst[4],float(lst[5]))
    data.append(entry)
call_list={1:op1 , 2:op2 ,3:op3,4:op4,5:op5,6:op6,7:op7,8:op8,9:op9,10:op10}
while(1):
    print("-"*90) 
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
    print("-"*90) 
    opt=int(input("Enter a query[1-10] [0-exit]: "))
    print("-"*90) 
    if(opt==0):
        print(data[0].score)
        break
    call_func(call_list[opt],data)