#버튼으로 색상 변경
'''
빨강, 파랑, 초록 버튼을 눌러 원의 색상을 바꾸시오.
'''

import tkinter as tk

def change_color(color):
    canvas.itemconfig(circle, fill=color)

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()
circle = canvas.create_oval(100,100,200,200, fill="gray")

tk.Button(root, text="빨강", command=lambda: change_color("red")).pack(side="left")
tk.Button(root, text="파랑", command=lambda: change_color("blue")).pack(side="left")
tk.Button(root, text="초록", command=lambda: change_color("green")).pack(side="left")

root.mainloop()
