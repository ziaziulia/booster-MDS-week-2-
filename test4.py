list = input().lower().split()
a = []

for x in list:
    if x not in a:
        a.append(x)
        print("{} {}".format(x, list.count(x)))