import itertools

for combination in itertools.product(range(10), repeat=2):
    print(''.join(map(str, combination)))
