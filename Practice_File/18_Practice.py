#도형 이동 프로그램 (MovingShapeApp)
'''
Canvas 위에 원형 도형(oval) 생성

키보드 이벤트로 도형 이동 (↑↓←→)

마우스 드래그로 색상·크기 변경'''

import tkinter as tk
import random

class MovingShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Shape")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.shape = self.canvas.create_oval(150,150,250,250, fill="pink")

        # 키보드 이벤트 바인딩
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # 마우스 이벤트 바인딩
        self.canvas.bind("<B1-Motion>", self.change_color)

    def move_up(self, event):
        self.canvas.move(self.shape, 0, -10)

    def move_down(self, event):
        self.canvas.move(self.shape, 0, 10)

    def move_left(self, event):
        self.canvas.move(self.shape, -10, 0)

    def move_right(self, event):
        self.canvas.move(self.shape, 10, 0)

    def change_color(self, event):
        color = random.choice(["red", "blue", "green", "yellow", "orange", "purple"])
        self.canvas.itemconfig(self.shape, fill=color)

root = tk.Tk()
app = MovingShapeApp(root)
root.mainloop()
