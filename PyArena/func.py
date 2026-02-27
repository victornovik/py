def yell(text):
    return text.upper() + '!'


funcs = [yell, str.lower, str.capitalize]
for f in funcs:
    print(f, f('hEy ThErE'))


# Callable object
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_3 = Adder(3)
print("Object is callable:", callable(plus_3))
print(plus_3(4))
