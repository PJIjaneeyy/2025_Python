#마우스로 도형 크기 조절
'''
마우스로 드래그하면 원의 크기를 변경하시오.
좌클릭 = 커짐 / 우클릭 = 작아짐
'''

import tkinter as tk

class ResizeCircleApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.circle = self.canvas.create_oval(150,150,250,250, fill="skyblue")
        self.size = 100

        self.canvas.bind("<B1-Motion>", self.grow)
        self.canvas.bind("<B3-Motion>", self.shrink)

    def grow(self, e):
        self.size += 5
        self.canvas.coords(self.circle, 200-self.size/2, 200-self.size/2, 200+self.size/2, 200+self.size/2)

    def shrink(self, e):
        if self.size > 20:
            self.size -= 5
            self.canvas.coords(self.circle, 200-self.size/2, 200-self.size/2, 200+self.size/2, 200+self.size/2)

root = tk.Tk()
app = ResizeCircleApp(root)
root.mainloop()
