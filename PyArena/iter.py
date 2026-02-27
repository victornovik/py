import itertools
import random
import timeit
from functools import reduce

dic = {'a': [1, 2, 1], 'b': [3, 4, 1], 'c': [5, 6, 2]}


def ret_all_gt_than_1():
    return [(k, v) for k, v in dic.items() if all(x > 1 for x in v)]


def ret_any_gt_than_2():
    return [(k, v) for k, v in dic.items() if any(x > 2 for x in v)]


print("ret_all_gt_than_1", ret_all_gt_than_1())
print("ret_any_gt_than_2", ret_any_gt_than_2())

# Pick odd matrix elements
matrix = [[1, 2], [3, 4], [5, 6]]
print("odd matrix elements", [x for row in matrix for x in row if x % 2 == 1])


nums = [(-3, -2), (-2, -1), (-1, 0), (1, 2), (2, 5), (3, 4)]

# map(), starmap(), list comprehension
def squares_map():
    return list(map(lambda k: k[0] * k[1], nums))


def squares_starmap():
    return list(itertools.starmap(lambda k1, k2: k1 * k2, nums))


def squares_comprehension():
    return [k[0] * k[1] for k in nums]


print("Time spent on squares_map: ", timeit.timeit(squares_map, number=1000))
print("Time spent on squares_starmap: ", timeit.timeit(squares_starmap, number=1000))
print("Time spent on squares_comprehension: ", timeit.timeit(squares_comprehension, number=1000))

# filter(), list comprehension
evens = filter(lambda k: k[0] % 2 == 0, nums)
vowels = [ch for ch in "Hello world" if ch in 'aeiou']
replaceAllButVowels = [ch if ch in 'aeiou' else 'X' for ch in "Hello world"]

# walrus operator in list comprehension
hotTemperatures = [temp for _ in range(20) if (temp := random.randrange(90, 110)) > 100]
print("T more than 100:", hotTemperatures)

# reduce()
print(reduce(lambda x, y: x + y, [1, 2, 3]))

# filter, map, reduce
print("Filter, map and reduce:",
      reduce(lambda x, y: x + y, map(lambda x: x + x, filter(lambda x: (x >= 3), [1, 2, 3, 4]))))

# Iterators
# print("How iterators work")
# d = [5, 3, 7, 10, 32]
# it = iter(d)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break


class InfiniteSquaring:
    def __init__(self, initial):
        self.num = initial

    def __next__(self):
        self.num = self.num ** 2
        return self.num

    def __iter__(self):
        return self


sq = InfiniteSquaring(2)
# print(next(sq))

# Generators
# squares_gen = (i ** 2 for i in range(11))
# for i in squares_gen:
#     print(i)


def generator():
    i = 1
    while True:
        yield i
        i += 1


gen = generator()
for i in range(5):
    print("Generate next:", next(gen))

# nums = {-1: 1, 2: 2, -3: 3}
# res = {index: v * 2 for index, v in enumerate(nums)}
# print(res)
#
# res = {k: v * 10 for k, v in nums.items()}
# print(res)
#
# res = [i for i in nums if i > 0]
# print(res)
#
# for i in range(5):
#     print(i)
