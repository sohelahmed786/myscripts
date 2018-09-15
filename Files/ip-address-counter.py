
from collections import Counter
items=[]
with open("net2001.dst",'r') as f:
    for line in f:
        items.append(line)

s = Counter(items)
top_five = s.most_common(5)
print(top_five)
