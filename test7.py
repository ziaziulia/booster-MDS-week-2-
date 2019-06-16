c = str()
d = []
a = 0
b = 0
r = 0
t = 0
with open('D:\\text.txt') as inf:
    for line in inf:
        line = line.strip()
        c = line.split(';')
        f = (int(c[1])+int(c[2])+int(c[3]))/3
        print(f)
        a += int(c[1])
        r += int(c[2])
        t += int(c[3])
        b += 1
print(a/b,r/b,t/b)