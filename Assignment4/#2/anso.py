from stud import Contact

def display(data):
    header="{:<15}{:<15}{:<30}{:<15}"
    print("_"*70)
    print(header.format("ID-No","Name","Email-Id","Phone_No"))
    print("_"*70)
    for i in data:
        print(header.format(i.id,i.name,i.email,i.phno))
    print("_"*70)

def create(data):
    entry=Contact()
    entry.id=input("Enter ID: ")
    entry.name=input("Enter Name: ")
    entry.email=input("Enter E-Mail ID: ")
    entry.phno=input("Enter phone number: ")
    data.append(entry)
    print("Data was added succesfully!")

def read(data):
    cmd=input("Show all?: ")
    if(cmd.casefold()=="y"):
        display(data)
        return 
    else:
        c=0
        name=input("Enter name/ID you want to search: ")
        for i in data:
            if(i.id==name or i.name==name):
                c+=1
                header="{:<15}{:<15}{:<30}{:<15}"
                print("_"*70)
                print(header.format("ID_no","Name","Email-Id","Phone_No"))
                print("_"*70)
                print(header.format(i.id,i.name,i.email,i.phno))
                print("_"*70)
        if c==0:
            print("No record matching the name/ID")
            
def update(data):
    id_=input('Enter the ID of record to update: ')
    cmd=input("What do you wanna update?: ")
    entry=input("Enter new data: ")
    for i in data:
        if(i.id.casefold()==id_.casefold()):
            if(cmd.casefold()=="name"):
                i.name=entry
                print("updated!")
                return
            elif(cmd.casefold()=="email" or cmd.casefold()=="email-id"):
                i.email=entry
                print("updated!")
                return
            elif(cmd.casefold()=="phone-number" or cmd.casefold()=="phone_no"):
                i.phno=entry
                print("updated!")
                return

def delete(data):
    id_=input('Enter the id number to delete: ')
    for i in data:
        if(i.id==id_):
            data.remove(i)
            print("Deleted!")
            return

def call(f,data):
    f(data)


dfile=open("D:/python/Assignment4/#2/data.txt.txt","r")
cont=dfile.readlines()
data=[]
for i in cont:
    lst=i.replace("\n","").split(",")
    data.append(Contact(lst[0],lst[1],lst[2],lst[3]))
display(data)
opt={1:create,2:read,3:update,4:delete}
while True:
    print("-"*70)
    cmd=int(input("1. Create 2. Read 3. Update 4. Delete 5. Exit: "))
    print("-"*70)
    if(cmd==5):
        break
    else:
        call(opt[cmd],data)
dfile.close()