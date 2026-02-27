# from classes import *
# from sys import getsizeof
# import copy

import stl.containers

print(stl.containers.pack_named_args(firstname="John", lastname="Doe", age=25))


def gen_greeting(name):
    return lambda greeting: f"{greeting} {name}"


print(gen_greeting("Victor")("Hi"))

# Print all non-magic methods
# print([p for p in dir(Path(".")) if not p.startswith('_')])

# print(str.__doc__)            # the same as print(help(str))
# print(type(v1))               # print the object type
# print(id(v1), id(v2))         # print the object address
# print(dir(__builtins__))      # print the attribute list
# print(Car.__subclasses__())   # print all subclasses
# print(car.__dict__)           # print all the fields of the instance with their values
# print(__name__)               # print current module name

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
