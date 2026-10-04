so_tuple = int(input("Nhap so tuple (x, y): "))
ds_tuple = []

for i in range(so_tuple):
    x = float(input("Nhap x: "))
    y = float(input("Nhap y: "))
    ds_tuple.append((x, y))

if ds_tuple:
    trung_binh_x = sum(toa_do[0] for toa_do in ds_tuple) / len(ds_tuple)
    trung_binh_y = sum(toa_do[1] for toa_do in ds_tuple) / len(ds_tuple)
    print("Trung binh cua x:", trung_binh_x)
    print("Trung binh cua y:", trung_binh_y)
else:
    print("Can nhap it nhat mot tuple.")