def foo():
    try:
        return 1
    finally:
        return 2

# print(foo())

def bar():
    yield 33
    return 55

for i in bar():
    print(i)

# it = bar()
# print(next(it))
# print(next(it))

# print(next(bar()))
# print(next(bar()))
# print(next(bar()))

# d = {1: 3, 1: 2}
# print(d)

listik = ['a', 'b']
my_tuple = ('max', 'min', listik, 'aaa')
listik.append('c')
print(my_tuple)

print([1, 2, 3] + [4, 5, 6])


def bar():
    yield 33
    return 55


for i in bar():
    print(i)

# print(4 + True)

# i = 5
# print(type(i))
# i = None
# print(type(i))

my_set = set('abc')
my_set.add('def')
my_set.add('a')
print(my_set)

def swap_two_var(a, b):
    print(f"Before swap a: {a}, b: {b}")
    a, b = b, a
    print(f"After swap a: {a}, b: {b}")


# split on separate words
# text = ["Life is beautiful", "No need to overthink", "Meditation helps in overcoming depression"]
# print([word for sentence in text for word in sentence.lower().split(' ')])
# print([word for sentence in text for word in sentence.lower().split(' ') if word not in ["is", "in", "to", "no"]])

# Find matching numbers
# x = [51, 24, 32, 41]
# y = [42, 32, 41, 50]
# print([i for i in x for j in y if i == j])

# x = [51, 24, 32, 41]
# print([1 if 30 < i < 45 else 0 for i in x])
