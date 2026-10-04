dict1 = {}
so_cap1 = int(input("Nhap so cap key-value cua dictionary thu nhat: "))

for i in range(so_cap1):
    key = input("Nhap key: ")
    value = int(input("Nhap gia tri: "))
    dict1[key] = value

dict2 = {}
so_cap2 = int(input("Nhap so cap key-value cua dictionary thu hai: "))

for i in range(so_cap2):
    key = input("Nhap key: ")
    value = int(input("Nhap gia tri: "))
    dict2[key] = value

dict_gop = dict1.copy()
for key, value in dict2.items():
    if key in dict_gop:
        dict_gop[key] += value
    else:
        dict_gop[key] = value

print("Dictionary sau khi gop:", dict_gop)