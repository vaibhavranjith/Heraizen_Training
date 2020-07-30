limit=int(input('Enter the upper bound number to generate the fibinacci numbers:\n'))
p=0
q=1
if limit==1:
    print(f"Fibonacci series upto {limit} terms")
    print(p)
else:
    print(f"Fibonacci series upto {limit} terms")
    while p <=limit :
        print(p,end=" ")
        p,q=q,p+q