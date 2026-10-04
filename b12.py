chuoi = input("Nhap mot chuoi: ")
tan_suat = {}

for ky_tu in chuoi:
    if ky_tu in tan_suat:
        tan_suat[ky_tu] += 1
    else:
        tan_suat[ky_tu] = 1

print("So lan xuat hien cua moi ky tu:", tan_suat)