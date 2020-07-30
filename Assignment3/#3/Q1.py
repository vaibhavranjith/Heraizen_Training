def get_digits(n):
    lst=[0]*4
    i=3
    while i>=0:
        lst[i]=n%10
        n=n//10
        i-=1
    return lst

def add(n):
    lst=get_digits(n)
    return sum(lst)

dig=[]
for i in range(0,9999):
    if(add(i)==12):
        dig=get_digits(i)
        if(dig[2]==abs(dig[0]-dig[1]) and dig[3]==(dig[0]+dig[2])):
            print(i)