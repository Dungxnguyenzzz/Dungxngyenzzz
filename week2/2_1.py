import math

print("2.1. Thể tích của hình cầu có bán kính r là bao nhiêu?")
r = float(input("Nhập bán kính: "))
P = (r ** 3) * (4 / 3) * math.pi

print(f"Thể tích của hình cầu là: {P:.2f}")
