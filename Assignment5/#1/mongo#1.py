import pymongo
from pymongo import MongoClient
from IPython.display import clear_output
# 1. Get empno,name,salary,dname, location of the all the employess
# 2. Get the total salary of the given dept
# 3. Get employee who are working in the given dname
# 4. Get max and min paid employee
# 5. Get count,max,min,avg salary of all the department
# 6. Get max salary paid department
# 7. Get the employee who are not reporting to anyone
# 8. Get job count of each department

def get_location(client,dno):
    filter={"deptno":dno}
    lst=list(client.employee.dept.find(filter))
    return lst[0]["location"]

def get_dname(client,dno):
    filter={"deptno":dno}
    lst=list(client.employee.dept.find(filter))
    return lst[0]["dname"]

def op1(client):
    pipe=[{
        '$project':{
            "empno":1,
            "ename":1,
            "sal":1,
            "deptno":1    
        }
    }]
    lst=list(client.employee.emp.aggregate(pipe))
    print("_"*100)
    header="{:<15}{:<15}{:<15}{:<15}{:<15}"
    print(header.format("ENo","Ename","Salary","Department","Location"))
    print("_"*100)
    for i in lst:
        print(header.format(i['empno'],i['ename'],i['sal'],get_dname(client,i['deptno']),get_location(client,i['deptno'])))
        print("-"*100)
    print("_"*100)
  
def op6(client):
    pipe=[{
        '$group':{
            '_id':"$deptno",
            "accum":{'$max':"$sal"}
        }},{
        '$group':{
            "_id":None,
            "max":{'$max':"$accum"}
        }
    }]
    lst=list(client.employee.emp.aggregate(pipe))
    mx=lst[0]['max']
    filter={"sal":mx}
    lst=list(client.employee.emp.find(filter))
    dname=get_dname(client,lst[0]["deptno"])
    print(f"The department that pays the highest salary: {dname}")
    
    
def op8(client):
    pipeline=[
        {
            '$group':{
                '_id':{"Dept No":"$deptno"},
                'count':{'$sum':1}    
            }
        }
    ]
    lst=list(client.employee.emp.aggregate(pipeline))     
    print("_"*80)
    header="{:<15}{:<15}"
    print(header.format("DeptNo","Count"))
    print("_"*80)
    for i in lst:
        print("-"*80)
        print(header.format(i['_id']['Dept No'],i['count']))
        
def op7(client):
    filter={'mgr':'NULL'} 
    lst=list(client.employee.emp.find(filter))
    header="{:<15}{:<15}{:<15}"
    print("_"*100)
    print(header.format("Eno","Ename","Job"))
    print("_"*100)
    for i in lst:
        print(header.format(i['empno'],i['ename'],i['job']))
        print("-"*100)
    print("_"*100)
    
def op3(client):
    dep=input("Enter the department")
    filter={"dname":dep}
    dlst=list(client.employee.dept.find(filter))
    dno=dlst[0]["deptno"]
    filter={"deptno":dno}
    header="{:<15}{:<15}{:<15}"
    print("_"*100)
    print(header.format("Emp No","Ename","Job"))
    print("_"*100)
    elst=list(client.employee.emp.find(filter))
    for i in elst:
        print(header.format(i["empno"],i["ename"],i["job"]))
        print("-"*100)
    print("_"*100)
def op2(client):
    dep=input("Enter the department")
    filter={"dname":dep}
    dlst=list(client.employee.dept.find(filter))
    dno=dlst[0]["deptno"]
    pipe=[
    {
        '$match': {
            'deptno': dno
        }
    }, {
        '$group': {
            '_id': 0, 
            'Amount': {
                '$sum': '$sal'
            }
        }
    }
    ]
    lst=list(client.employee.emp.aggregate(pipe))
    print(f"The {dep} department has a total salary of: {lst[0]['Amount']}")

def op4(client):
    pipe=[
    {
        '$group': {
            '_id': 0, 
            'Max': {
                '$max': '$sal'
            }, 
            'Min': {
                '$min': '$sal'
            }
        }
    }
    ]
    lst=list(client.employee.emp.aggregate(pipe))
    mxfilter={"sal":lst[0]['Max']}
    mnfilter={"sal":lst[0]['Min']}
    mxdocument=list(client.employee.emp.find(mxfilter))
    mndocument=list(client.employee.emp.find(mnfilter))
    print("_"*100)
    header="{:<15}{:<15}{:<15}"
    print(header.format("Emp-No","Ename","Salary"))
    print("_"*100)
    print(header.format(mxdocument[0]['empno'],mxdocument[0]['ename'],mxdocument[0]['sal']))
    print("-"*100)
    print(header.format(mndocument[0]['empno'],mndocument[0]['ename'],mndocument[0]['sal']))
    print("_"*100)

def op5(client):
    pipe=[
    {
        '$group': {
            '_id': '$deptno', 
            'Max': {
                '$max': '$sal'
            }, 
            'Min': {
                '$min': '$sal'
            }, 
            'Count': {
                '$sum': 1
            }, 
            'Average': {
                '$avg': '$sal'
            }
        }
    }
    ]
    lst=list(client.employee.emp.aggregate(pipe))
    header="{:<15}{:<15}{:<15}{:<15}{:<15}"
    print("_"*100)
    print(header.format("Department","Max","Min","Count","Average"))
    print("_"*100)
    for i in lst:
        print(header.format(get_dname(client,i["_id"]),i['Max'],i['Min'],i['Count'],i['Average']))
        print("-"*100)
    print("_"*100)


def call_f(f,client):
    f(client)   
#Establishin connection with the cluster
try :
    client =MongoClient("mongodb+srv://analytics:analytics-password@cluster0.labxu.mongodb.net/employee?retryWrites=true&w=majority")

except:
    print("Error in connecting to cluster")
opt={1:op1,2:op2,3:op3,4:op4,5:op5,6:op6,7:op7,8:op8}

while True:
        print("_"*100)
        print("1. Get empno,name,salary,dname, location of the all the employess")
        print("2. Get the total salary of the given dept")
        print("3. Get employee who are working in the given dname")
        print("4. Get max and min paid employee")
        print("5. Get count,max,min,avg salary of all the department")
        print("6. Get max salary paid department")
        print("7. Get the employee who are not reporting to anyone")
        print("8. Get job count of each department")
        print("_"*100)
        cmd=int(input("Enter a query [1-10] [0 -exit] :"))
        if(cmd==0):
            break
        if(cmd==11):
            clear_output()
            continue
        call_f(opt[cmd],client)