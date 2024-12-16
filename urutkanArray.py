# 1 dimensi
def urutkanArray1Dimensi():
    array = [5, 2, 9, 1, 5, 6]
    sorted_array = sorted(array)
    sorted_descending_array = sorted(array, reverse=True)
    print("ascending", sorted_array)
    print("descending", sorted_descending_array)
# 2 dimensi
def urutkanArray2Dimensi():
    array_2d = [[2,3,1], [5,7,6]]
    sorted_by_first = sorted(array_2d, key=lambda x : x[0])
    print("Urutkan berdasarkan elemen pertama ", sorted_by_first)

urutkanArray2Dimensi()


