class bank_account:
    def __init__(self, ten_tai_khoan, so_tai_khoan, ngan_hang, so_du):
        self.ten_tai_khoan = ten_tai_khoan
        self.so_tai_khoan = so_tai_khoan
        self.ngan_hang = ngan_hang
        self.so_du = so_du
        
    def __str__(self):
        return f"Tài khoản {self.ten_tai_khoan} tại ngân hàng {self.ngan_hang} với số tài khoản {self.so_tai_khoan} có số dư {self.so_du}"
        
    def thao_tac(self):
        chon = input("Bạn muốn rút tiền, gửi tiền hay kiểm tra số dư? (rút/gửi/kiểm tra): ")
        if chon.lower() == "rút":
            so_tien = float(input("Nhập số tiền bạn muốn rút: "))
            if so_tien > self.so_du:
                return "Số dư không đủ để rút."
            else:
                self.so_du -= so_tien
                return f"Bạn đã rút {so_tien}. Số dư hiện tại: {self.so_du}"
        elif chon.lower() == "gửi":
            so_tien = float(input("Nhập số tiền bạn muốn gửi: "))
            self.so_du += so_tien
            return f"Bạn đã gửi {so_tien}. Số dư hiện tại: {self.so_du}"
        elif chon.lower() == "kiểm tra":
            return f"Số dư hiện tại của bạn là: {self.so_du}"
        else:
            return "Lựa chọn không hợp lệ. Hãy chọn 'rút', 'gửi' hoặc 'kiểm tra'."

if __name__ == '__main__':
    so_tai_khoan = int(input("Nhập số lượng tài khoản: "))
    for i in range(so_tai_khoan):
        print(f"\nNhập thông tin tài khoản {i+1}:")
        tai_khoan = bank_account(
            input("Tên tài khoản: "), 
            input("Số tài khoản: "), 
            input("Ngân hàng: "), 
            float(input("Số dư: "))
        )
        print(tai_khoan)
        if i == 0:  # Chỉ thao tác thử với tài khoản đầu tiên
            print(tai_khoan.thao_tac())
