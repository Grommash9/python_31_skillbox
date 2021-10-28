import itertools
numbers = [i for i in range(0, 10)]

combination_list = itertools.permutations(numbers, 4)

for combination in combination_list:
    print(combination)
