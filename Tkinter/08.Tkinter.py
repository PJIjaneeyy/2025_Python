#키보드로 색상 변경 (R/G/B)
'''
R, G, B 키를 눌러 도형의 색상을 변경하시오.
'''

import tkinter as tk

def change_color(e):
    key = e.char.lower()
    if key == 'r': canvas.itemconfig(circle, fill="red")
    elif key == 'g': canvas.itemconfig(circle, fill="green")
    elif key == 'b': canvas.itemconfig(circle, fill="blue")

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()
circle = canvas.create_oval(100,100,200,200, fill="gray")
root.bind("<Key>", change_color)
root.mainloop()
