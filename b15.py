ds = [int(x) for x in input("Nhap cac so nguyen: ").split()]
ds_loc = [so for so in ds if so > 10 and so % 2 == 0]

print("Cac so chan lon hon 10:", ds_loc)