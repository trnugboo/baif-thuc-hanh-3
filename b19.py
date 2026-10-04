ds = [int(x) for x in input("Nhap cac so nguyen: ").split()]
N = int(input("Nhap N: "))

if len(ds) < 2:
    print("Can it nhat hai phan tu de tim cap.")
else:
    cap_gan_nhat = (ds[0], ds[1])
    tong_gan_nhat = ds[0] + ds[1]

    for i in range(len(ds)):
        for j in range(i + 1, len(ds)):
            tong = ds[i] + ds[j]
            if abs(tong - N) < abs(tong_gan_nhat - N):
                cap_gan_nhat = (ds[i], ds[j])
                tong_gan_nhat = tong

    print("Cap co tong gan N nhat:", cap_gan_nhat)
    print("Tong:", tong_gan_nhat)