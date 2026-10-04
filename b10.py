ds = [int(x) for x in input("Nhap cac so nguyen: ").split()]
tan_suat = {}

for so in ds:
    if so in tan_suat:
        tan_suat[so] += 1
    else:
        tan_suat[so] = 1

so_lan_nhieu_nhat = max(tan_suat.values())
phan_tu_nhieu_nhat = [so for so, so_lan in tan_suat.items() if so_lan == so_lan_nhieu_nhat]

print("Phan tu xuat hien nhieu nhat:", phan_tu_nhieu_nhat)
print("So lan xuat hien:", so_lan_nhieu_nhat)