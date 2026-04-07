import time

print("5.1. Tính số ngày từ Epoch và thời gian hiện tại")
sumtime = time.time()
giay = 60
phut = 60 * giay
gio = 60 * phut
ngay = 24 * gio

so_ngay = int(sumtime // ngay)
giay_con_lai = sumtime % ngay

so_gio = int(giay_con_lai // gio)
giay_con_lai = giay_con_lai % gio

so_phut = int(giay_con_lai // phut)
giay_con_lai = giay_con_lai % phut

so_giay = int(giay_con_lai)

print(f"Số ngày đã trôi qua kể từ Epoch: {so_ngay} ngày")
print(f"Thời gian hiện tại (GMT): {so_gio:02d}:{so_phut:02d}:{so_giay:02d}") 
print(f"Thời gian hiện tại (Việt Nam): {(so_gio + 7) % 24:02d}:{so_phut:02d}:{so_giay:02d}")
