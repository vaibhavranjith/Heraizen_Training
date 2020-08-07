import pymongo
from pymongo import MongoClient

def op1(col):
    name=input("Enter the team name: ")
    label=input("Enter the team label: ")
    city=input("Enter the city: ")
    coach=input("Enter the coach of the team: ")
    home=input("Enter the home: ")
    col.insert_one({"name":name,"label":label,"home":home,"city":city,"coach":coach})

def op2(col):
    name=input("Enter the team name: ")
    col.delete_one({"name":name})

def op3(col):
    name=input("Enter the name of the team to update: ")
    opt=int(input("What do you wanna update[1-5]: "))
    print("1. Name  2. Label  3. City 4. Coach 5. Home ")
    new=input("Enter the new field: ")
    if(opt==1):
        col.update_one({"name":name},{"$set":{"name": new}})
    elif opt==2:
        col.update_one({"name":name},{"$set":{"label": new}})
    elif opt==3:
        col.update_one({"name":name},{"$set":{"city": new}})
    elif opt==4:
        col.update_one({"name":name},{"$set":{"coach": new}})
    else:
        col.update_one({"name":name},{"$set":{"home": new}})

def op4(col):
    rd=input("Enter the name of the team name to see it's details: ")
    res=list(col.find({"name":rd}))
    print(type(res))
    print("{:<30}{:<30}".format("Name",res[0]["name"]))
    print("{:<30}{:<30}".format("Label",res[0]["label"]))
    print("{:<30}{:<30}".format("City",res[0]["city"]))
    print("{:<30}{:<30}".format("Coach",res[0]["coach"]))
    print("{:<30}{:<30}".format("Home",res[0]["home"]))

def op5(col):
    name=input("Enter the player name: ")
    label=input("Enter the team label: ")
    price=float(input("Enter his price: "))
    role=input("Enter the player's role: ")
    col.insert_one({"name":name,"label":label,"price":price,"role":role})

def op6(col):
    name=input("Enter the name of the player to update: ")
    opt=int(input("What do you wanna update[1-5]: "))
    print("1. Name  2. Price  3. Role 4. Label ")
    new=input("Enter the new field: ")
    if(opt==1):
        col.update_one({"name":name},{"$set":{"name": new}})
    elif opt==2:
        col.update_one({"name":name},{"$set":{"price": float(new)}})
    elif opt==3:
        col.update_one({"name":name},{"$set":{"role": new}})
    else :
        col.update_one({"name":name},{"$set":{"label": new}})

def op7(col):
    name=input("Enter the player name: ")
    col.delete_one({"name":name})
    

def op8(col):
    rd=input("Enter the name of the player to see it's details: ")
    res=list(col.find({"name":rd}))
    print(type(res))
    print("{:<30}{:<30}".format("Name",res[0]["name"]))
    print("{:<30}{:<30}".format("Label",res[0]["label"]))
    print("{:<30}{:<30}".format("Price",res[0]["price"]))
    print("{:<30}{:<30}".format("Role",res[0]["role"]))

def call_f(f,col):
    f(col)

client=MongoClient("mongodb+srv://analytics:analytics-password@cluster0.labxu.mongodb.net/Ipl?retryWrites=true&w=majority")
players=client.Ipl.players
teams=client.Ipl.teams
ipl=client.Ipl.ipl
opt={1:op1,2:op2,3:op3,4:op4,5:op5,6:op6,7:op7,8:op8}
while True:
    print("1. Add team ")
    print("2. Delete team")
    print("3. Update team")
    print("4. Read team")
    print("5. Add player")
    print("6. Update player")
    print("7. Delete player")
    print("8. Read player")
    cmd=int(input("Enter an operation[1-8] [0-exit]: "))
    if cmd==0:
        break
    if cmd>=1 and cmd<=4:
        call_f(opt[cmd],teams)
    if cmd>=5 and cmd<=8:
        call_f(opt[cmd],players )




