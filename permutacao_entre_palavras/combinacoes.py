import itertools

result = itertools.permutations('ABC', 3)

for comb in result:
    print(''.join(comb))