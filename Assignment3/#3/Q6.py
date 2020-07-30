#6
import functools
lst=list(map(int,input("Enter the list: ").split(" ")))
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lst)) 