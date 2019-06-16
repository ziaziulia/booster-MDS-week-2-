d = {'север':0,'юг':0,'восток':0,'запад':0}
a = int(input())
i = 0
while i<a:
    b = input()
    c = b.split()
    d[c[0]]+=int(c[1])
    i+=1
print(int(d['восток'])-int(d['запад']),int(d['север'])-int(d['юг']),end='')