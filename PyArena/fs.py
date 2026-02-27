# import shutil
# from os import path
from pathlib import Path


def is_dir_empty(path: str) -> bool:
    return not any(Path(path).iterdir())


# Iterate through the contents of the directory
for f in Path('.').iterdir():
    print(f)

# Current working directory
print("Current working dir:", Path.cwd())

# create a new file
# name = Path('./test.txt')
# if name.exists():
#     name.unlink()
# # name.touch()
#
# # create a new file and open it for writing
# with open(name, "x") as file:
#     file.write("first line")
#     file.write("second line")
#
# with open(name, "r") as file:
#     print(file.read())

# d = Path('files')
# if not d.exists():
#     d.mkdir()
#
# f1 = d / 'first.txt'
# f2 = d / 'second.txt'
# for p in [f1, f2]:
#     with open(p, 'w') as file:
#         file.write('1-st line\n')
#         file.write('2-nd line\n')
#
# with open(f1, 'r') as file:
#     print(file.read())
# with open(f2, 'r') as file:
#     while True:
#         line = file.readline()
#         print(line.upper())
#         if not line:
#             break
#
# shutil.rmtree(d, ignore_errors=True)


# for p in [f1, f2]:
#     p.unlink()
#
# if is_dir_empty(d.__str__()):
#     d.rmdir()

# with open(s, 'w') as file:
#     file.write('test line\n')
#     file.write('test line\n')
#
# with open(s, 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

# Create a list where every file line placed in a separate list element
# with open('json.json', 'r') as file:
#     print(file.readlines())

# d = Path('D:/') / 'dev' / 'src' / 'Python' / 'pyArena' / 'django'
# if not d.exists():
#     d.mkdir()
#     d.rmdir()

# print(Path(".").absolute())
# print(Path('D:/') / 'dev' / 'src')
# print(Path('D:\\dev\\src\\Python\\PyArena').exists())
# print(Path('D:\\dev\\src\\Python\\PyArena\\fs.py').is_file())
# print(Path('D:\\dev\\src\\Python\\PyArena').is_dir())
