#Q7
import functools
lst=list(map(int,input("Enter the list: ").split(" ")))
s=0
lst=list(filter(lambda i: i%2==0,lst))
if(len(lst)>1):
    (functools.reduce(lambda a,b :a**2+(b**2),lst)) 
else:
    print(lst[0]**2)