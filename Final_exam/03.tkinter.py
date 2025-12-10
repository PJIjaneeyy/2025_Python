# [문제 3 변형] Shape 계층 오버라이딩 + 둘레(perimeter())만 표시
import tkinter as tk
import math

# 1. 클래스 구조
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        raise NotImplementedError("하위 클래스에서 둘레 계산 메서드를 구현해야 합니다.")
    
    # 원본 문제의 draw() 및 area()는 생략하고 perimeter()에 집중

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def perimeter(self):
        # 다형성 구현 1: 직사각형 둘레 오버라이딩
        return 2 * (self.w + self.h)

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def perimeter(self):
        # 다형성 구현 2: 원 둘레 오버라이딩
        return 2 * math.pi * self.r

class App:
    def __init__(self, master):
        master.title("문제3 변형: 도형 둘레 계산")
        master.geometry("300x200")

        # 고정 좌표 및 크기 (원본 문제 참고)
        self.rect = Rectangle(50, 50, 100, 60) # w=100, h=60
        self.circle = Circle(150, 110, 40)    # r=40
        
        self.shape_var = tk.StringVar(value="Rectangle") 

        # UI 구성
        tk.Label(master, text="도형을 선택하고 둘레를 계산하세요.").pack(pady=10)

        frame_radio = tk.Frame(master)
        frame_radio.pack(pady=5)
        
        tk.Radiobutton(frame_radio, text="직사각형 (W=100, H=60)", variable=self.shape_var, value="Rectangle").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_radio, text="원 (R=40)", variable=self.shape_var, value="Circle").pack(side=tk.LEFT, padx=10)
        
        tk.Button(master, text="둘레 계산", command=self.calculate_perimeter, width=15).pack(pady=10)

        self.result_label = tk.Label(master, text="결과가 여기에 표시됩니다.", fg="red")
        self.result_label.pack(pady=5)

    def calculate_perimeter(self):
        selected = self.shape_var.get()
        
        if selected == "Rectangle":
            shape_obj = self.rect
        else:
            shape_obj = self.circle
        
        # 다형적 호출: perimeter()를 통해 각 도형의 둘레 계산
        calculated_perimeter = shape_obj.perimeter()
        
        # 결과 출력 (둘레만 표시)
        self.result_label.config(text=f"둘레={calculated_perimeter:.2f}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()