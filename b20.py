matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

kich_thuoc = len(matrix)
tong_duong_cheo_chinh = sum(matrix[i][i] for i in range(kich_thuoc))
tong_duong_cheo_phu = sum(matrix[i][kich_thuoc - 1 - i] for i in range(kich_thuoc))
tuple_matrix = tuple(tuple(hang) for hang in matrix)

print("Tong duong cheo chinh:", tong_duong_cheo_chinh)
print("Tong duong cheo phu:", tong_duong_cheo_phu)
print("Tuple cua tuple:", tuple_matrix)