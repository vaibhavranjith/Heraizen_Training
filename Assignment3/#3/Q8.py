
def Pascal(n) :  
    for line in range(0, n) : 
        r=str()
        for i in range(0, line + 1) :  
            r=r+str(binc(line, i))+" "
        print("{:^100}".format(r), end = "") 
        print() 
      
def binc(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 

n = int(input("Enter number of rows: "))
Pascal(n)
