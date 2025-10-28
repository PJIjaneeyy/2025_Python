#도형 이동 + 색상 변경
'''
Canvas 위에 원을 그리고, 방향키로 이동시키며
스페이스바를 누르면 색상이 랜덤으로 바뀌게 하시오
'''
import tkinter as tk
import random

class MovingCircleApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.circle = self.canvas.create_oval(150,150,250,250, fill="pink")

        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.change_color)

    def move_up(self, e): self.canvas.move(self.circle, 0, -10)
    def move_down(self, e): self.canvas.move(self.circle, 0, 10)
    def move_left(self, e): self.canvas.move(self.circle, -10, 0)
    def move_right(self, e): self.canvas.move(self.circle, 10, 0)
    def change_color(self, e):
        color = random.choice(["red","blue","green","yellow","orange","purple"])
        self.canvas.itemconfig(self.circle, fill=color)

root = tk.Tk()
app = MovingCircleApp(root)
root.mainloop()
