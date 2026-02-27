import math
import random
import secrets
import string


def rec_factorial(i):
    if i == 1:
        return 1
    return i * rec_factorial(i - 1)


print(math.factorial(5))
print(rec_factorial(5))

# generate random sequence
CHARS = string.ascii_letters + string.digits + string.punctuation
print("".join(secrets.choice(CHARS) for _ in range(8)))
print("".join(random.choices(CHARS, k=8)))

# print(random.choice("abcdef"))
# print(random.choice([1, 2, 3]))

# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)
# print(nums)
#
# print(random.randint(1, 10))
