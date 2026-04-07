class car:
    def __init__(self, hang, kich_thuoc, mau, gia):
        self.hang = hang
        self.kich_thuoc = kich_thuoc
        self.mau = mau
        self.gia = gia
        
    def __str__(self):
        return f"Đã tạo xe {self.hang} với kích thước {self.kich_thuoc}, màu {self.mau} và giá {self.gia}"
        
    def toc_do(self):
        dieu_chinh_toc_do = input("Bạn muốn tăng tốc hay giảm tốc ? (tăng/giảm): ")
        if dieu_chinh_toc_do.lower() == "tăng":
            return "Bạn đã tăng tốc"
        elif dieu_chinh_toc_do.lower() == "giảm":
            return "Bạn đã giảm tốc"
        else:
            return "Quyết định không hợp lệ. Hãy chọn 'tăng' hoặc 'giảm'."
            
    def dam(self):
        print("Xe đằng trước chạy hơi láo !")
        suy_nghi = input("Bạn có muốn đâm không ? (có/không): ")
        if suy_nghi.lower() == "có":
            return "Bạn đã quyết định đâm, xe đã có bảo hiểm thân vỏ, yên tâm !"
        elif suy_nghi.lower() == "không":
            return "Bạn đã quyết định không đâm, thôi a di đà phật"
        else:
            return "Quyết định không hợp lệ. Hãy chọn 'có' hoặc 'không'."

if __name__ == '__main__':
    so_xe = int(input("Nhập số lượng xe: "))
    for i in range(so_xe):
        print(f"Nhập thông tin xe {i+1}:")
        xe = car(input("Hãng xe: "), input("Kích thước: "), input("Màu: "), input("Giá: "))
        print(xe)
        
        if i == 0:  # Tương tác với xe đầu tiên
            print(xe.toc_do())
            print(xe.dam())
