#이미지 자동 슬라이드 쇼
'''
Label 위에 이미지 표시

여러 이미지를 리스트로 관리

after() 메서드로 일정 시간마다 변경'''

import tkinter as tk
from PIL import Image, ImageTk

class ImageSlideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("슬라이드 쇼")

        self.images = [ImageTk.PhotoImage(file=f"img{i}.png") for i in range(1,5)]
        self.index = 0

        self.label = tk.Label(root, image=self.images[self.index])
        self.label.pack()

        self.update_image()

    def update_image(self):
        self.index = (self.index + 1) % len(self.images)
        self.label.config(image=self.images[self.index])
        self.root.after(2000, self.update_image)

root = tk.Tk()
app = ImageSlideApp(root)
root.mainloop()
