def binarySearch(data,p):
    c=0
    for i in range(0,len(data)):
        pattern=True
        if(i+len(p)<len(data)+1):
            for j in range(0,len(p)):
                if(data[i+j]!=p[j]):
                    pattern=False
        if pattern and i+len(p)<len(data)+1 :
            c+=1
    print(c)

vowels=['a','e','i','o','u']
s=input("Enter data:")
for i in s:
    if i in vowels:
        s=s.replace(i,"0")
    else:
        s=s.replace(i,"1")
print("Modified: "+s)
p=input("Enter a pattern:")
print(binarySearch(s,p))


