so_san_pham = int(input("Nhap so san pham: "))
so_luong_theo_sku = {}

for i in range(so_san_pham):
    sku = input("Nhap SKU: ")
    quantity = int(input("Nhap quantity: "))
    if sku in so_luong_theo_sku:
        so_luong_theo_sku[sku] += quantity
    else:
        so_luong_theo_sku[sku] = quantity

ds_san_pham = list(so_luong_theo_sku.items())
print("Danh sach SKU khong trung:", ds_san_pham)