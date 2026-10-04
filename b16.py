diem_sinh_vien = {}
so_sinh_vien = int(input("Nhap so sinh vien: "))

for i in range(so_sinh_vien):
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem: "))
    diem_sinh_vien[ten] = diem

ds_sap_xep = sorted(diem_sinh_vien.items(), key=lambda muc: muc[1], reverse=True)

print("Danh sach sinh vien theo diem giam dan:")
for ten, diem in ds_sap_xep:
    print(ten, diem)