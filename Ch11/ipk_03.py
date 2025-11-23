import tkinter as tk
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def draw(self, canvas):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def draw(self, canvas):
        x1, y1 = self.x, self.y
        x2, y2 = self.x + self.w, self.y + self.h
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="tomato")

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2 * math.pi * self.r

    def draw(self, canvas):
        x1, y1 = self.x - self.r, self.y - self.r
        x2, y2 = self.x + self.r, self.y + self.r
        canvas.create_oval(x1, y1, x2, y2, outline="black", fill="skyblue")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("문제3")
        self.geometry("300x220")
        self.config(bg='white')
        
        self.canvas = tk.Canvas(self, width=280, height=140, bg="white", borderwidth=1, relief="solid")
        self.canvas.pack(pady=10)
        
        self.shape_var = tk.StringVar(value="Rectangle") 

        radio_frame = tk.Frame(self, bg='white')
        radio_frame.pack()
        
        tk.Radiobutton(radio_frame, text="사각형", variable=self.shape_var, value="Rectangle", bg='white').pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(radio_frame, text="원", variable=self.shape_var, value="Circle", bg='white').pack(side=tk.LEFT, padx=10)

        tk.Button(self, text="그리기", command=self.draw_shape).pack(pady=5)
        
        self.result_label = tk.Label(self, text="도형을 선택하고 그리기를 누르세요.", font=('Arial', 10), bg='white')
        self.result_label.pack()

    def draw_shape(self):
        self.canvas.delete("all")
        
        selected_shape = self.shape_var.get()
        shape = None
        
        if selected_shape == "Rectangle":
            shape = Rectangle(x=50, y=50, w=100, h=60)
        elif selected_shape == "Circle":
            shape = Circle(x=150, y=70, r=40) 

        if shape:
            shape.draw(self.canvas)
            
            area = shape.area()
            perimeter = shape.perimeter()
            
            result_text = f"면적={area:.2f}, 둘레={perimeter:.2f}"
            self.result_label.config(text=result_text)

if __name__ == "__main__":
    app = App()
    app.mainloop()