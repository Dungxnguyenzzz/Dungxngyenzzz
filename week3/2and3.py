class Sieu_Nhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten 
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac
        
    def __str__(self):
        return f"Gao: {self.ten}, Vũ khí: {self.vu_khi}, Màu sắc: {self.mau_sac}"

if __name__ == '__main__':
    team = []
    so_sieu_nhan = int(input("Nhập số lượng siêu nhân Gao: "))
    
    for i in range(so_sieu_nhan):
        print(f"Nhập thông tin siêu nhân Gao {i+1}:")
        sieu_nhan = Sieu_Nhan(
            input("Nhập tên siêu nhân: "), 
            input("Nhập vũ khí của siêu nhân: "), 
            input("Nhập màu sắc của siêu nhân: ")
        )
        team.append(sieu_nhan)
        
    print("\n=== DANH SÁCH SIÊU NHÂN ===")
    for s in team:
        print(s)
