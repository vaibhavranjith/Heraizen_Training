import pymongo
from pymongo import MongoClient
from IPython.display import clear_output
import pprint
# 	5. Get all team details
def op1(client):
    lst=list(client.Ipl.ipl.aggregate([{'$group':{'_id':"$label"}}])) 
    print("Labels")
    print("-"*7)
    for i in lst:
        print(i['_id'])
        

def op2(client):
    n=input("Enter a team name: ")
    lst=list(client.Ipl.ipl.aggregate([{'$match':{"name":n}}]))  
    print("_"*25)
    print("Players")
    print("_"*25)
    for i in lst[0]['players']:
        print(i['name'])

def op3(client):
    team=input("Enter a team name: ")
    pipe=[
    {
        '$unwind': {
            'path': '$players'
        }
    }, {
        '$match': {
            'name': team
        }
    }, {
        '$group': {
            '_id': '$players.role', 
            'count': {
                '$sum': 1
            }
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipe))
    print("_"*100)
    header="{:<15}{:<15}"
    print(header.format("Role","Count"))
    print("_"*100)
    for i in lst:
        print(header.format(i["_id"],i["count"]))
        print("-"*100)
    print("_"*100)

def op4(client):
    team=input("Enter a team : ")
    role=input("Enter the role: ")
    pipe=[
    {
        '$match': {
            'name': team
        }
    }, {
        '$unwind': {
            'path': '$players'
        }
    }, {
        '$match': {
            'players.role': role
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipe))
    print("_"*100)
    header="{:25}{:<15}"
    print(header.format("Name","Price"))
    print("_"*100)
    for i in lst:
        print(header.format(i["players"]["name"],i["players"]["price"]))
        print("-"*100)
    print("_"*100)

def op5(client):
    pipe=[
    {
        '$project': {
            'players': 0
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipe))
    print("_"*130)
    header="{:<25}{:<25}{:<45}{:<30}"
    print(header.format("City","Coach","Home","Name"))
    print("_"*130)
    for i in lst:
        print(header.format(i["city"],i["coach"],i["home"],i["name"]))
        print("-"*130)
    print("_"*130)
def op6(client):
    pipeline=[{
        '$project':{ 
            '_id':0,
            "Name":"$name",
            "count":{'$sum':"$players.price"}
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipeline))
    print("_"*80)
    print("{:<30}{:<15}".format("Team Name","Amount"))
    print("_"*80)
    for i in lst:
        print("-"*80)
        print("{:<30}{:<15}".format(i["Name"],i["count"]))
    print("_"*80)
    
def op7(client):
    team=input("Enter the team name: ")
    role=input("Enter the role: ")
    pipe=[
    {
        '$match': {
            'name': team
        }
    }, {
        '$unwind': {
            'path': '$players'
        }
    }, {
        '$match': {
            'players.role': role
        }
    }, {
        '$group': {
            '_id': 0, 
            'Ammount': {
                '$sum': '$players.price'
            }
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipe))
    print("_"*100)
    a=lst[0]["Ammount"]
    print(f"The amount spent by {team} on the role {role} is: {a} ")
    print("_"*100)
def op9(client):
    pipe=[
    {
        '$unwind': {
            'path': '$players'
        }
    }, {
        '$group': {
            '_id': '$players.role', 
            'fieldN': {
                '$max': '$players.price'
            }
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipe))
    print("_"*100)
    print("{:<30}{:<15}{:<15}".format("Name","Price","Role"))
    print("_"*100)
    for i in lst:

        pipe2=[
            {
                '$unwind': {
                'path': '$players'
            }
            }, {
                '$match': {
                    'players.role': i["_id"], 
                    'players.price': i["fieldN"]
                 }
            }
            ]
        l=list(client.Ipl.ipl.aggregate(pipe2))
        n=l[0]["players"]["name"]
        print("{:<30}{:<15}{:<15}".format(n,i["fieldN"],i["_id"]))
        print("-"*100)
    print("_"*100)
def op8(client):
    key=input("Enter the key : ")
    key="players."+key
    pipe=[
    {
        '$unwind': {
            'path': '$players'
        }
    }, {
        '$sort': {
            key: 1
        }
    }
    ]
    lst=list(client.Ipl.ipl.aggregate(pipe))
    print("_"*100)
    print("{:<30}{:<15}{:<15}".format("Name","Price","Role"))
    print("_"*100)
    for i in lst:
        print("{:<30}{:<15}{:<15}".format(i["players"]["name"],i["players"]["price"],i["players"]["role"]))
        print("-"*100)
    print("_"*100)

def callf(f,client):
    f(client)
    
client=MongoClient("mongodb+srv://analytics:analytics-password@cluster0.labxu.mongodb.net/Ipl?retryWrites=true&w=majority")
fs={1:op1,2:op2,3:op3,4:op4,5:op5,6:op6,7:op7,8:op8,9:op9}
while True:
    
    print("_"*80)
    print("1. Get all team labels")
    print("2. Get all players of the given team")
    print("3. Get Role wise count of the given team")
    print("4. Get player details by role and team")
    print("5. Get all team details")
    print("6. Get amount spent by each team")
    print("7. Get amount spent by each team")
    print("8. Display all the player details sorted by given feild")
    print("9. Get Max paid players of all roles")
    print("_"*80)
    cmd=int(input("Enter a query [1-9] [0-exit]: "))
    if(cmd==0):
        break
    if(cmd==11):
        clear_output()
        continue
    callf(fs[cmd],client)