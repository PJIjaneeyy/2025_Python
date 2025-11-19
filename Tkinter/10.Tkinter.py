#버튼으로 애니메이션 실행
'''
“시작” 버튼을 누르면 텍스트 색상과 크기가 10번 바뀌는 애니메이션 실행.
'''

import tkinter as tk
import random
import time

def animate_text():
    for i in range(10):
        color = random.choice(["red","blue","green","purple","orange"])
        size = random.randint(20,80)
        canvas.itemconfig(text_id, fill=color, font=("Helvetica", size))
        canvas.update()
        time.sleep(0.5)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()
text_id = canvas.create_text(200,100, text="Animation!", font=("Helvetica",40))
tk.Button(root, text="시작", command=animate_text).pack()
root.mainloop()
