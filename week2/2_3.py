print("2.3. Tính giờ về đến nhà sau khi chạy bộ") 
TIME1 = float(input("Nhập giờ xuất phát: "))
TIME2 = float(input("Nhập phút xuất phát: ")) 
EASYRUN1 = float(input("Nhập số dặm chạy dễ ban đầu: "))
MIDRUN = float(input("Nhập số dặm chạy bình thường: "))
EASYRUN2 = float(input("Nhập số dặm chạy dễ lúc sau: "))

# Quy đổi tất cả ra giây
TIMEEND = TIME1 * 3600 + TIME2 * 60 + EASYRUN1 * (8 * 60 + 15) + MIDRUN * (7 * 60 + 12) + EASYRUN2 * (8 * 60 + 15)

if TIME1 >= 0 and TIME2 >= 0 and EASYRUN1 > 0 and MIDRUN >= 0 and EASYRUN2 >= 0:
    HOUR = int(TIMEEND // 3600 % 24)
    MINUTE = int(TIMEEND % 3600 // 60)
    SECOND = int(TIMEEND % 60)
    print(f"Bạn về ăn sáng lúc: {HOUR:02d}:{MINUTE:02d}:{SECOND:02d}")
else: 
    print("Nhập sai rồi bố ơi !")
