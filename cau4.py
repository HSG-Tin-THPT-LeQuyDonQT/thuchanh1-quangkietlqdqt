can_nang = float(input("Nhap can nang cua ban (kg): "))
chieu_cao = float(input("Nhap chieu cao cua ban (m): "))
BMI = round(can_nang / (chieu_cao ** 2),2)
if BMI < 18.5:
    print("Ban bi gay")
elif BMI < 25:
    print("Ban binh thuong")
else:
    print("Ban hoi thua can")
