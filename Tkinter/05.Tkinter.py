#자동 이미지 슬라이드쇼
'''
4개의 이미지를 2초마다 자동으로 변경하시오.
'''

import tkinter as tk
from PIL import Image, ImageTk

class SlideApp:
    def __init__(self, root):
        self.root = root
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
SlideApp(root)
root.mainloop()
