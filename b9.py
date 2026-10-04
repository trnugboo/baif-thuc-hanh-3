ds = [int(x) for x in input("Nhap cac so nguyen: ").split()]
ds_khong_trung = []

for so in ds:
    if so not in ds_khong_trung:
        ds_khong_trung.append(so)

print("List sau khi loai trung:", ds_khong_trung)