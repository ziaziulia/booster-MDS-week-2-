import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/603.txt')
b = r.text
c = b.splitlines()
print(len(c))