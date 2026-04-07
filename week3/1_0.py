import math 

class point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        print(f"Đã tạo điểm tại ({self.x}, {self.y})")
        
    def distance(self, x1, y1):
        return math.hypot(self.x - x1, self.y - y1)

if __name__ == '__main__':
    x = float(input("Nhập tọa độ x của điểm A : "))
    y = float(input("Nhập tọa độ y của điểm A : "))
    Tam = point(0, 0)
    my_circle = point(x, y)
    
    distance1 = math.hypot(x, y)
    
    x1 = float(input("Nhập tọa độ x của điểm B: "))
    y1 = float(input("Nhập tọa độ y của điểm B: "))
    distance2 = my_circle.distance(x1, y1)
    
    print(f"Khoảng cách từ điểm ({x}, {y}) đến gốc toạ độ O là: {distance1:.2f}")
    print(f"Khoảng cách từ điểm B ({x1}, {y1}) đến điểm A ({x}, {y}) là: {distance2:.2f}")
