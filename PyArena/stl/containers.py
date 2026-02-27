def merge_lists_to_dict(keys, values):
    res = dict(zip(keys, values))
    return res


# Create dictionary from named arguments, where arg name is a key and arg value is a value
def pack_named_args(**items):
    return items


def filter_list_std(list_to_filter, type_to_filter) -> list:
    return list(filter(lambda elem: type(elem) is type_to_filter,
                       list_to_filter))


def unpack_list(name, qty):
    print(name, qty)


def unpack_dict(name, qty):
    print(name, qty)

# unpack_list(*["Victor", 5])
# unpack_dict(**{"name": "Victor", "qty": 25})
# one, *others = [1, 2, 3]
# x, y = (1, 2)
