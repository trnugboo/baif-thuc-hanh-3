thong_tin = {}

for i in range(3):
    ten = input("Nhap ten nguoi thu " + str(i + 1) + ": ")
    tuoi = int(input("Nhap tuoi: "))
    thong_tin[ten] = tuoi

print(thong_tin)