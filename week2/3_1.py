print("3.1. Vẽ lưới 2x2")
Dong = '+' + '-' * 4 + '+' + '-' * 4 + '+'
XuongDong = '|' + ' ' * 4 + '|' + ' ' * 4 + '|'

def ve1():
    print(Dong)
    for i in range(4):
        print(XuongDong)
    print(Dong)
    for i in range(4):
        print(XuongDong)
    print(Dong)

ve1()
