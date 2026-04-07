class cho:
    def __init__(self, ten, mau, loai, cam_xuc):
        self.ten = ten
        self.mau = mau
        self.loai = loai
        self.cam_xuc = cam_xuc
        
    def __str__(self):
        return f"Tên: {self.ten}, Loài: {self.loai}, Màu: {self.mau}, Cảm xúc: {self.cam_xuc}"
        
    def choc_cho(self):
        quyet_dinh = input(f"Bạn muốn chọc, cho ăn hay vỗ {self.ten}? (chọc/cho ăn/vỗ): ")
        if quyet_dinh.lower() == "chọc":
            self.cam_xuc = "tức giận"
            return f"Bạn đã chọc {self.ten}, nó đang {self.cam_xuc} và sắp cắn bạn, chạy nhanh lên =)) !"
        elif quyet_dinh.lower() == "cho ăn":
            self.cam_xuc = "hạnh phúc"
            return f"Bạn đã cho ăn {self.ten}, nó đang {self.cam_xuc} và vẫy đuôi !"
        elif quyet_dinh.lower() == "vỗ":
            self.cam_xuc = "vui vẻ"
            return f"Bạn đã vỗ {self.ten}, nó đang {self.cam_xuc} và lăn ngửa cho bạn xoa bụng !"
        else:
            return "Quyết định không hợp lệ. Hãy chọn 'chọc', 'cho ăn' hoặc 'vỗ'."
            
    def sua(self):
        return f"{self.ten} đang sủa: Gâu gâu!"
        
    def an(self, thuc_an):
        self.thuc_an = thuc_an
        return f"{self.ten} đang ăn {thuc_an}."
        
    def choi(self, do_choi):
        self.do_choi = do_choi
        return f"{self.ten} đang chơi với {do_choi}."

if __name__ == '__main__':
    chuong_cho = []
    so_cho = int(input("Nhập số lượng chó: "))
    
    for i in range(so_cho):
        print(f"\n--- Nhập thông tin bé {i+1} ---")
        co_ho = cho(input("Nhập tên chó: "), input("Nhập màu chó: "), input("Nhập loài chó: "), "bình thường")
        chuong_cho.append(co_ho)
        
    print("\n=== DANH SÁCH CHUỒNG CHÓ ===")
    for c in chuong_cho:
        print(c)
        
    if len(chuong_cho) > 0:
        print("\n--- Tương tác ---")
        print(chuong_cho[0].choc_cho())
