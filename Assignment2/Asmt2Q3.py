s="Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked"
lt=s.split(" ")
a=set(lt)
for val in a:
    c=0
    print(f"{val} occurs:")
    for i in lt:
        if(i==val):
            c+=1
    print(c)

