import tkinter as tk

#기본 윈도우 생성
root = tk.Tk()
root.title("Tkinter 예제")
root.geometry("200x100")

#라벨(Label) 하나 추가
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

#이벤트 루프 실행
root.mainloop()
