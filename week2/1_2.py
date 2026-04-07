print("1.2. Chuyển đổi x KM sang miles, biết 1 mile bằng 1.61 km")
x = float(input("Nhập số kilometers: "))
y = x / 1.61

if y == 1:
    print(f"{x} km bằng {y} mile")
else:
    print(f"{x} km bằng {y} miles")
