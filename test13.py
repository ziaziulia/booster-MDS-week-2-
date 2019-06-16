dictionary = {input().lower() for i in range(int(input()))}
words_ = [input().lower().split() for j in range(int(input()))]
words = {w for wl in words_ for w in wl}
print(*(words - dictionary), sep ='\n')