ds = input("Nhap cac phan tu trong list: ").split()
ds_dao_nguoc = []

for i in range(len(ds) - 1, -1, -1):
    ds_dao_nguoc.append(ds[i])

print("List sau khi dao nguoc:", ds_dao_nguoc)