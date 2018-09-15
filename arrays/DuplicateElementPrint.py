import collections

freq = collections.Counter(['a','b','c','a'])
for k in freq:
    if freq[k] > 1:
        print(k) # prints "a"
        break
