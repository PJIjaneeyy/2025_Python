#텍스트 애니메이션

'''
텍스트 크기와 색상 변경

after()나 time.sleep() 이용

랜덤 색상/크기 변화'''

import tkinter as tk
import random
import time

def animate_text():
    for i in range(10):
        update_text_size()
        update_text_color()
        canvas.update()
        time.sleep(0.5)

def update_text_size():
    new_size = random.randint(20, 80)
    canvas.itemconfig(text_id, font=("Helvetica", new_size))

def update_text_color():
    color = random.choice(["red", "blue", "green", "purple", "orange"])
    canvas.itemconfig(text_id, fill=color)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

text_id = canvas.create_text(200, 100, text="Hello Tkinter!", font=("Helvetica", 40))
animate_text()

root.mainloop()
