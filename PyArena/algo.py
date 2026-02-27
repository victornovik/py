import itertools

# Написать функцию, которая на вход принимает строку вида "AAABBCCCC", и возвращает "3А2В4С".
from collections import defaultdict, Counter

import pytest

 
def count(input_str: str) -> str:
    cnt = defaultdict(int)
    new_str = ""
    for char in input_str:
        cnt[char] += 1
    for key, value in cnt.items():
        new_str = new_str + f"{value}{key}"
    return new_str

def count_v2(input_str: str) -> str:
    new_str = ""
    cnt = Counter(input_str)
    for key, value in cnt.items():
        new_str = new_str + f"{value}{key}"
    return new_str

print(count("AAABBCCCC"))

@pytest.mark.parametrize("input_str,result", [
    ("AAABBCCCC", "3A2B4C"),
    ("AAA", "3A"),
    ("", ""),
    ("ABBCCCC", "1A2B4C"),
    ("AAABBC", "3A2B1C")])
def test_count(input_str: str, result: str):
    assert count_v2(input_str) == result



# def compress_plain(s: str) -> str:
#     count = 1
#     prev = s[0]
#     res = ""
#
#     for ch in s[1:]:
#         if ch == prev:
#             count += 1
#         else:
#             res += str(count) + prev
#             count = 1
#         prev = ch
#
#     res += str(count) + prev
#     return res

def count_itertools(s: str) -> str:
    return str().join([str(len(el)) + el[0] for el in [list(g) for _, g in itertools.groupby(s)]])

    # res = ""
    # for el in [list(g) for k, g in itertools.groupby(s)]:
    #     res += str(len(el)) + el[0]
    # return res

# compress_itertools("АААВВССССDAAAAAAAABBB")
assert count_itertools("АААВВССССDAAAAAAAABBB") == '3А2В4С1D8A3B'


def reverse_str(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def is_palindrome_2(s: str) -> bool:
    for idx, ch in enumerate(s[::-1]):
        if s[idx] != ch:
            return False
    return True


# print(is_palindrome("a"))
# print(is_palindrome("abcda"))
# print(is_palindrome("abcba"))
# print(is_palindrome("abcddcba"))

assert is_palindrome("арозаупаланалапуазора")
assert is_palindrome("дискоксид")
