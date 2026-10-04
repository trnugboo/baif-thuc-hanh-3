set1 = {int(x) for x in input("Nhap cac so nguyen cua set thu nhat: ").split()}
set2 = {int(x) for x in input("Nhap cac so nguyen cua set thu hai: ").split()}

print("Giao:", set1 & set2)
print("Hop:", set1 | set2)
print("Hieu set1 - set2:", set1 - set2)
print("Hieu set2 - set1:", set2 - set1)