import json
from emp import employee
from emp import department
# 1. Get empno,name,salary,dname, location of the all the employess
# 2. Get the total salary of the given dept
# 3. Get employee who are working in the given dname
# 4. Get max and min paid employee
# 5. Get count,max,min,avg salary of all the department
# 6. Get max salary paid department
# 7. Get the employee who are not reporting to anyone
# 8. Get job count of each department

def op1(ddata):
    header="{:<15}{:<15}{:<15}{:<30}{:<15}"
    print("_"*100)
    print(header.format("Emp-No","Name","Salary","Department-Name","Location"))
    print("_"*100)
    for j in ddata:
       for i in j.emplst:
            print("-"*100)
            print(header.format(i.empno,i.ename,i.sal,j.dname,j.location))
    print("_"*100)  

def op2(ddata):
    header="{:<15}{:<15}"
    print("_"*40)
    print(header.format("Department","Total Salary"))
    print("_"*40)
    for i in ddata:
        s=0
        for j in i.emplst:
            s+=j.sal
        print("-"*40)
        print(header.format(i.dname,s))
    print("_"*40)

def op3(ddata):
    dep=input("Enter the department you want: ")
    header="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
    print("_"*100)
    print(header.format("Emp-No","Name","Job","Manager","Hire-date","Salary","Comm"))
    print("_"*100)
    for i in ddata:
        if i.dname==dep:
            for j in i.emplst:
                print("-"*100)
                print(header.format(j.empno,j.ename,j.job,j.mgr,j.hiredate,j.sal,j.comm))
            break
    print("_"*100)

def op4(ddata):
    mx=0.0
    mn=float('inf')
    for j in ddata:
        for i in j.emplst:
            if(i.sal>mx):
                mx=i.sal
            if(i.sal<mn):
                mn=i.sal
    header="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
    print("_"*100)
    print(header.format("Emp-No","Name","Job","Manager","Hire-date","Salary","Comm"))
    print("_"*100)
    for i in ddata:
        for j in i.emplst:
                if j.sal==mx:
                    print("-"*100)
                    print(header.format(j.empno,j.ename,j.job,j.mgr,j.hiredate,j.sal,j.comm))
    for i in ddata:
        for j in i.emplst:
                if j.sal==mn:
                    print("-"*100)
                    print(header.format(j.empno,j.ename,j.job,j.mgr,j.hiredate,j.sal,j.comm))
    print("_"*100)

def op5(ddata):
    header="{:<15}{:<15}{:<15}{:<15}{:<15}"
    print("_"*80)
    print(header.format("Department","Count","Max","Min","Average"))
    print("_"*80)
    for i in ddata:
        lst=[]
        for j in i.emplst:
            lst.append(j.sal)
        if(len(lst)>0):
            print("-"*80)
            print(header.format(i.dname,len(lst),max(lst),min(lst),round(sum(lst)/len(lst),2)))
    print("_"*80)  

def op6(ddata): 
    mx=0
    print("The department with highest salary is :")
    for i in ddata:
        lst=[]
        for j in i.emplst:
            lst.append(j.sal)
        
        if(len(lst)>0 and max(lst)>mx):
            mx=max(lst)
    for i in ddata:
        lst=[]
        for j in i.emplst:
            lst.append(j.sal)
        if(len(lst)>0 and max(lst)==mx):
            print("{:<15}{:<15}".format(i.dname,max(lst)))
    
        
def op7(ddata):
    header="{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}"
    print("_"*100)
    print(header.format("Emp-No","Name","Job","Manager","Hire-date","Salary","Comm"))
    print("_"*100)
    for i in ddata:
        for j in i.emplst:
            if(j.mgr=="NULL"):
                print(header.format(j.empno,j.ename,j.job,j.mgr,j.hiredate,j.sal,j.comm))
    print("_"*100)
            
def op8(ddata):
    header="{:<15}{:<15}{:<15}"
    print("_"*80)
    print(header.format("Dept-No","Department","Number of jobs"))
    print("_"*80)
    for i in ddata:
        print("-"*80)
        print(header.format(i.deptno,i.dname,len(i.emplst)))
    print("_"*80)

def call_func(f,ddata):
    f(ddata)

def init_data(edata,ddata):
    for  i in edata:
        for j in ddata:
            if(i.deptno==j.get_deptno()):
                j.emplst.append(i)

with open("d:/python/Assignment5/#1/emp.json","r") as file:
    elst=json.load(file)
with open("d:/python/Assignment5/#1/dept.json","r") as file:
    dlst=json.load(file)

edata=[]
ddata=[]
for i in elst:
    if(i["comm"]=="NULL"):
        entry=employee(i["empno"],i["ename"],i["job"],i["mgr"],i["hiredate"],float(i["sal"]),-1,i["deptno"])
    else:
        entry=employee(i["empno"],i["ename"],i["job"],i["mgr"],i["hiredate"],float(i["sal"]),float(i["comm"]),i["deptno"])
    edata.append(entry)
for i in dlst:
    entry=department(i["deptno"],i["dname"],i["location"])
    ddata.append(entry)
init_data(edata,ddata)
opt={1:op1,2:op2,3:op3,4:op4,5:op5,6:op6,7:op7,8:op8}
while True:
    print("_"*100)
    print(" 1. Get empno,name,salary,dname, location of the all the employess")
    print(" 2. Get the total salary of the given dept")
    print(" 3. Get employee who are working in the given dname")
    print(" 4. Get max and min paid employee")
    print(" 5. Get count,max,min,avg salary of all the department")
    print(" 6. Get max salary paid department")
    print(" 7. Get the employee who are not reporting to anyone")
    print(" 8. Get job count of each department")
    print("-"*100)
    cmd=int(input("Enter query[1-8] [0-exit]: "))
    if(cmd==0):
        break
    call_func(opt[cmd],ddata)