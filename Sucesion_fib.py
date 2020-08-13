def fibo(x):
    if x==0 or x==1:
        l.append(1)
        return 1
    else:
        l.append(fibo(x-1))
        
        return l[x-1]+l[x-2]
l=[]
s=4
print(fibo(s))

