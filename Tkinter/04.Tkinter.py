#카운터 프로그램
'''
“+”, “–” 버튼을 눌러 숫자를 증가/감소시키고
Label에 현재 숫자를 표시하시오.
'''

import tkinter as tk

count = 0

def increase():
    global count
    count += 1
    label.config(text=count)

def decrease():
    global count
    count -= 1
    label.config(text=count)

root = tk.Tk()
label = tk.Label(root, text=count, font=("Arial", 30))
label.pack()

tk.Button(root, text="+", command=increase).pack(side="left", padx=10)
tk.Button(root, text="-", command=decrease).pack(side="right", padx=10)

root.mainloop()

