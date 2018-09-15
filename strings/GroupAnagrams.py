def groupAnagrams(str):
    d = {}
    for item in str:
        s = "".join(sorted(item))
        if s not in d:
            d[s] = []
        d[s].append(item)
    print(d.values())

if __name__ == "__main__":
    words = ['abc', 'cab', 'cafe', 'goo', 'face']
    groupAnagrams(words)
