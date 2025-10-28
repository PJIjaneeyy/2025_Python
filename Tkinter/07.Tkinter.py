#텍스트 애니메이션 (색상 + 크기)
'''
텍스트의 색상과 크기가 10번 랜덤으로 바뀌는 애니메이션을 만드시오.
'''

import tkinter as tk
import random
import time

def animate_text():
    for i in range(10):
        new_size = random.randint(20,80)
        new_color = random.choice(["red","blue","green","orange","purple"])
        canvas.itemconfig(text_id, font=("Helvetica", new_size), fill=new_color)
        canvas.update()
        time.sleep(0.5)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()
text_id = canvas.create_text(200,100, text="Hello Tkinter!", font=("Helvetica",40))
animate_text()
root.mainloop()
