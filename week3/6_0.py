class NhanVien:
    LUONG_MAX = 50000000
    
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong
        
    def get_tenNhanVien(self):
        return self.tenNhanVien
        
    def set_tenNhanVien(self, tenNhanVien):
        self.tenNhanVien = tenNhanVien
        
    def get_luongCoBan(self):
        return self.luongCoBan
        
    def set_luongCoBan(self, luongCoBan):
        self.luongCoBan = luongCoBan
        
    def get_heSoLuong(self):
        return self.heSoLuong   
        
    def set_heSoLuong(self, heSoLuong):
        self.heSoLuong = heSoLuong
        
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong
        
    def inTTin(self):
        print("\n--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Tên nhân viên : {self.tenNhanVien}")
        print(f"Lương cơ bản  : {self.luongCoBan:,.0f} VNĐ")
        print(f"Hệ số lương   : {self.heSoLuong}")
        print(f"Tổng lương    : {self.tinhLuong():,.0f} VNĐ")
        
    def tangLuong(self, delta):
        luong_moi = self.luongCoBan * (self.heSoLuong + delta)
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Thông báo: Tăng lương thất bại! Mức lương mới ({luong_moi:,.0f} VNĐ) vượt quá mức tối đa quy định.")
            return False
        else:
            self.heSoLuong += delta
            return True

if __name__ == '__main__':
    nv1 = NhanVien(
        input("Nhập tên nhân viên: "), 
        float(input("Nhập lương cơ bản (VNĐ): ")), 
        float(input("Nhập hệ số lương: "))
    )
    nv1.inTTin()
    
    print("\n=> Đang thử tăng hệ số lương thêm 1.0...")
    ket_qua_1 = nv1.tangLuong(1.0)
    if ket_qua_1:
        print("Tăng lương thành công!")
        nv1.inTTin()
        
    print("\n=> Đang thử tăng hệ số lương thêm 2.0...")
    ket_qua_2 = nv1.tangLuong(2.0)
    if not ket_qua_2:
        print("Đã bị hệ thống từ chối.")
