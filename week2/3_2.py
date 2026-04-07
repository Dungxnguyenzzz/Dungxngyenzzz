print("3.2. Viết hàm vẽ lưới tùy chỉnh n hàng, m cột")
S_LINE = '+' + '-' * 4 
E_LINE = '+'
S_BLOCK = '|' + ' ' * 4 
E_BLOCK = '|'

Hang = int(input("Nhập số cột (số ô theo chiều ngang): "))
Cot = int(input("Nhập số hàng (số ô theo chiều dọc): "))

def ve2():
    for _ in range(Cot):
        for _ in range(Hang):
            print(S_LINE, end='')
        print(E_LINE)
        for _ in range(4):
            for _ in range(Hang):
                print(S_BLOCK, end='')
            print(E_BLOCK)
    # Vẽ dòng chốt cuối cùng
    for _ in range(Hang):
        print(S_LINE, end='') 
    print(E_LINE)

ve2()
