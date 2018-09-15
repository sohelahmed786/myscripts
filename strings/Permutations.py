from itertools import permutations

perms = [''.join(p) for p in permutations('abc')]
print(perms)
