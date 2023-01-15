import itertools
numbers = [i for i in range(10)]
n = 1_000_000

permutations = itertools.permutations(range(10), 10)

print(''.join(map(str,list(permutations)[n-1])))
