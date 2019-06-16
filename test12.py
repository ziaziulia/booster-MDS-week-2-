a = input()
b = input()
c = input()
d = input()
e = list(a)
f = list(b)
k = list(c)
l = list(d)
aa = len(e)
h = {}
hh = {}
i = 0
ii = 0
iii = 0
while i < aa:
	h[e[i]]=f[i]
	hh[f[i]]=e[i]
	i+=1
m = len(k)
while ii<m:
	print(h.get(k[ii]),end='')
	ii+=1
print()
n = len(l)
while iii<n:
	print(hh.get(l[iii]),end='')
	iii+=1