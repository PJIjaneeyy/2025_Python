#입력값을 이용한 텍스트 표시
'''
Entry에 이름을 입력하고 “출력” 버튼을 누르면
Canvas에 “안녕하세요, [이름]님!” 출력하시오.
'''

import tkinter as tk

def show_text():
    name = entry.get()
    canvas.delete("all")
    canvas.create_text(150,100, text=f"안녕하세요, {name}님!", font=("맑은 고딕", 20))

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="출력", command=show_text).pack()
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()
root.mainloop()
