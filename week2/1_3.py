print("1.3. Tính Pace và Speed trung bình dựa trên khoảng cách và thời gian")
Q = float(input("Nhập số KM đã chạy: ")) / 1.61
m = float(input("Nhập số phút đã chạy: "))
n = float(input("Nhập số giây đã chạy: "))

print(f"PACE là {(m + n / 60) / Q} mile/minutes") 
print(f"Tốc độ trung bình là {(m * 60 + n) / Q} mile/seconds") 
print(f"Tốc độ trung bình là {Q / ((m * 60 + n) / 3600):.2f} mile/hours")
