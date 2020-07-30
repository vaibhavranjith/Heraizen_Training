def display(data):
    header="{:<15}{:<15}{:<30}{:<15}"
    print("_"*70)
    print(header.format("ID_no","Name","Email-Id","Phone_No"))
    print("_"*70)
    for i in data:
        print(header.format(*i))
    print("_"*70)
def create(data):
    id_=input("Enter ID: ")
    name=input("Enter Name: ")
    email=input("Enter E-Mail ID: ")
    pno=input("Enter phone number: ")
    data.append([id_,name,email,pno])
def read(data):
    cmd=input("Show all?: ")
    if(cmd.casefold()=="y"):
        display(data)
        return
    else:
        name=input("Enter name/ID you want to search: ")
        for i in data:
            if(i[0]==name or i[1]==name):
                header="{:<15}{:<15}{:<30}{:<15}"
                print("_"*70)
                print(header.format("ID_no","Name","Email-Id","Phone_No"))
                print("_"*70)
                print(header.format(*i))
                print("_"*70)
def update(data):
    id_=input('Enter the ID of record to update: ')
    cmd=input("What do you wanna update?: ")
    entry=input("Enter new data: ")
    for i in data:
        if(i[0].casefold()==id_.casefold()):
            if(cmd.casefold()=="name"):
                print("updated!")
                i[1]=entry
                return
            elif(cmd.casefold()=="email" or cmd.casefold()=="email-id"):
                print("updated!")
                i[2]=entry
                return
            elif(cmd.casefold()=="phone-number" or cmd.casefold()=="phone_no"):
                print("updated!")
                i[3]=entry
                return
def delete(data):
    id_=input('Enter the id number to delete: ')
    for i in data:
        if(i[0]==id_):
            print(i)
            data.remove(i)
            print("Deleted!")
            return

dfile=open("D:/python/Assignment3/#4/data.txt.txt","r")
cont=dfile.readlines()
data=[]
for i in cont:
    data.append(i.replace("\n","").split(","))
display(data)
while True:
    print("-"*70)
    cmd=int(input("1. Create 2. Read 3. Update 4. Delete 5. Exit: "))
    print("-"*70)
    if(cmd==5):
        break
    elif(cmd==1):
        create(data)
    elif(cmd==2):
        read(data)
    elif(cmd==3):
        update(data)
    else:
        delete(data)
dfile.close()