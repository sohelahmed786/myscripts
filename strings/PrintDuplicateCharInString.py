import collections

freq = collections.Counter("abcda")
for k in freq:
    if freq[k] > 1:
        print(k) # prints "a"
        break
