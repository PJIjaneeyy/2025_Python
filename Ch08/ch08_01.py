import tkinter as tk
import random

class MovingShapeApp:
    def __init__(self, root):
        # 1. 초기 설정: 메인 윈도우(root) 설정
        self.root=root
        self.root.title("Moving Shape")

        #캔버스 생성
        self.canvas = tk.Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack()

        # 원형 도형 (타원, oval)을 캔버스에 생성하고 ID를 인스턴스 변수에 저장합니다.
        # 이 ID(self.shape)는 도형을 이동하거나 속성을 변경할 때 사용됩니다.
        #원
        self.shape = self.canvas.create_oval(100,100,200,200, fill="pink")

        #이벤트 처리를 위한 상태 변수
        # 방향키를 각 이동 메서드에 연결
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        #마우스 이벤트
        self.canvas.bind("<B1-Motion>", self.change_color)



    #이동 메서드
    #도형을 이동시키고 외곽선을 변경하는 내부 공통 메서드
    def move_shape(self,dx,dy):
        self.canvas.move(self.shape,dx,dy)

    def move_up(self, event):
        self.move_shape(0,-10)

    def move_down(self, event):
        self.move_shape(0,10)

    def move_left(self, event):
        self.move_shape(-10,0)

    def move_right(self, event):
        self.move_shape(10,0)

    #색 변경 메서드
    def change_color(self,event):
        colors = ["red","orange","blue","pink","purple","yellow"]
        color = random.choice(colors)
        self.canvas.itemconfig(self.shape,fill=color)


root = tk.Tk()
app = MovingShapeApp(root)
root.mainloop()