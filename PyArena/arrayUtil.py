from array import array

arr = array('i', [4, 3, 2, 1, 3])
print("Count of 3:", arr.count(3))

arr.reverse()
print(arr)

with open("array.bin", "wb") as file:
    arr.tofile(file)

imported_arr = array('i')
with open("array.bin", "rb") as file:
    imported_arr.fromfile(file, 3)
