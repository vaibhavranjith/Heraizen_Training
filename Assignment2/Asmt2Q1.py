data={  "cs_dept":{1001,1002,1005,1008,1010},
        "is_dept":{1010,1002,1005,1015,1020},
        "ec_dept":{1002,1005,1015,1010,1003}
    }
#a
common=set(data["cs_dept"])
values=data.values()
for val in values:
    common=common.intersection(val)    
print(common)

#b
faculty=set(data["cs_dept"])
for val in values:
    faculty=faculty.union(val)
print(len(faculty))

#c
print(set(data["cs_dept"]).union(set(data["is_dept"]))-set(data["ec_dept"]))