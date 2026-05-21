n = int(input("Nhap so co 4 chu so bat ki: "))
tong = 0
tong = tong + n % 10
n = n // 10
tong = tong + n % 10
n = n // 10
tong = tong + n % 10
n = n // 10
tong = tong + n
print("tong cua 4 chu so do la: ",tong)
