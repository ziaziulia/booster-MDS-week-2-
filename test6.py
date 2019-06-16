s = input()
a = len(s)
b=0
i = 0
T=['A']
b = 1
while i<a:
    if s[i]<T[0]:
        k=int(s[i])
        f=1
        if d==1:
            e = int(c*10+k-(1*c))
            f=0
            print(b*e,end='')
        print(str(b*k*f),end='')
        i+=1
        d=1
        c=k
    else:
        b=s[i]
        i+=1
        d=0
