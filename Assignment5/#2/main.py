import json
from ipl import team
#   1. Get all the team labels
# 	2. Get all players of the given team
# 	3. Get role wise count of given team
# 	4. Get Player details by role and team
# 	5. Get all team details
# 	6. Get amount spent by each team
# 	7. Get amount spent on role by the team
# 	8. Display all the player details sory by given field
# 	9. Get Max Paid players of all roles
def line(n=80,t=0):
    if t==0:
        print("-"*n)
    else:
        print("_"*n)

def op1(data):
    line(30,1)
    print("{:<15}".format("Label"))
    line(30,1)
    for i in data:
        line(30)
        print("{:<15}".format(i.label))
    line(30,1)

def op2(data):
    tm=input("Enter the name of the team: ")
    line(30,1)
    print("Players")
    line(30,1)
    for i in data:
        if i.name==tm:
            for j in i.players:
                line(30)
                print(j["name"])
            break
    line(30,1)

def op3(data):
    line(100,1)
    # header="{:<30}{:<15}{:<20}{:<15}{:<15}"
    header="{:<30}{:^15}{:^20}{:^15}{:^15}"
    print(header.format("Team","Batsman","Wicket Keeper","All-Rounder","Bowler"))
    line(100,1)
    for i in data:
        c={"Batsman":0,"Wicket Keeper":0,"All-Rounder":0,"Bowler":0}
        for j in i.players:
            c[j["role"]]+=1
        line(100)
        print(header.format(i.name,c["Batsman"],c["Wicket Keeper"],c["All-Rounder"],c["Bowler"]))
    line(100,1)
        

def op4(data):
    line(80,1)
    header="{:<30}{:<35}{:<15}"
    print(header.format("Player","Team","Role"))
    line(80,1)
    for i in data:
        for j in i.players:
            line()
            print(header.format(j["name"],i.name,j["role"]))
    line(80,1)

def op5(data):
    header="{:<25}{:<15}{:<15}"
    for i in data:
        line(100,1)
        print(f"City: {i.city} ")
        print(f"Coach: {i.coach} ")
        print(f"Home:  {i.home}")
        print(f"Name: {i.name}")
        print(f"Label: {i.label}")
        line(100)
        print(header.format("Player Name","Price","Role"))
        line(100)
        for j in i.players:
            print(header.format(j["name"],j["price"],j["role"]))
        line(100,1)

def op6(data):
    header="{:<30}{:<15}"
    line(80,1)
    print(header.format("Team name","Amount"))
    line(80,1)
    for i in data:
        s=0
        for j in i.players:
            s+=j["price"]
        line(80)
        print(header.format(i.name,s))
    line(80,1)

def op7(data):
    header="{:<30}{:<15}{:<25}{:<15}{:<15}"
    line(100,1)
    print(header.format("Team name","Batsman","Wicket Keeper","All-Rounder","Bowler"))
    line(100,1)
    for i in data:
        s={"Batsman":0,"Wicket Keeper":0,"All-Rounder":0,"Bowler":0}
        for j in i.players:
            s[j["role"]]+=j["price"]
        line(100)
        print(header.format(i.name,s["Batsman"],s["Wicket Keeper"],s["All-Rounder"],s["Bowler"]))
    line(100,1)

def ele0(e):
    return e[0]
def ele1(e):
    return e[1]
def ele2(e):
    return e[2]

def op8(data):
    cmd=input("Enter the key to sort:: ")
    lst=[]
    for i in data:
        for j in i.players:
            lst.append((j["name"],j["price"],j["role"]))
    op={"name":ele0,"price":ele1,"role":ele2}
    srt_lst=sorted(lst,key=op[cmd])
    line(80,1)
    header="{:<25}{:<20}{:<15}"
    print(header.format("Name","Price","Role"))
    line(80,1)
    for i in srt_lst:
        line(80)
        print(header.format(i[0],i[1],i[2]))
    line(80,1)

def op9(data):
    mx={"Batsman":0,"Wicket Keeper":0,"All-Rounder":0,"Bowler":0}
    for i in data:
        for j in i.players:
            if(mx[j["role"]]<j["price"]):
                mx[j["role"]]=j["price"]
    line(100,1)
    header="{:<25}{:<30}{:<20}"
    print(header.format("Role","Player","Price"))
    line(100,1)
    for i in data:
        for j in i.players:
            if(mx[j["role"]]==j["price"]):
                line(100)
                print(header.format(j["role"],j["name"],j["price"]))
    line(100)


def call_func(f,data):
    f(data)

with open("d:/python/Assignment5/#2/ipl2020.json","r") as file:
    tlst=json.load(file)
#loading data
data=[]
for i in tlst:
    entry=team(i["city"],i["coach"],i["home"],i["name"],i["label"])
    for j in i["players"]:
        entry.players.append(j)
    data.append(entry)
opt={1:op1,2:op2,3:op3,4:op4,5:op5,6:op6,7:op7,8:op8,9:op9}
while True:
    print("_"*100)
    print("1. Get all the team labels")
    print("2. Get all players of the given team")
    print("3. Get role wise count of given team")
    print("4. Get Player details by role and team")
    print("5. Get all team details")
    print("6. Get amount spent by each team")
    print("7. Get amount spent on role by the team")
    print("8. Display all the player details sory by given field")  
    print("9. Get Max Paid players of all roles")
    print("_"*100)
    cmd=int(input("Enter an option[1-9] [0-exit]: "))
    if cmd==0:
        break
    call_func(opt[cmd],data)