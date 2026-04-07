print("2.2. Tính giá tiền sách (có giảm giá 40% và tính phí vận chuyển)")
sach = input("Nhập số sách cần mua: ")

if sach.isdigit():
    S = int(sach)
    if S >= 1:
        tong_tien = (S * 24.95 * 0.6) + 3 + ((S - 1) * 0.75)
        print(f"Tổng số tiền là: {tong_tien:.2f} Đô")
    else: 
        print("Em không bán sách nửa cuốn sách anh ạ!")
else:
    print("Em không bán nửa cuốn đâu !")
