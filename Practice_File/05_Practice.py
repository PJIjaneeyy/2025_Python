#마우스 클릭으로 캔버스 도형 속성 변경 (색상)

import tkinter as tk

# 전역 위젯 및 상태 변수
canvas = None
circle_id = None
# 현재 색상 상태를 추적하는 플래그 (False=초기색/Green, True=Red)
is_red = False 

def toggle_color(event):
    global canvas, circle_id, is_red
    
    # 1. 현재 상태(is_red)에 따라 다음 색상을 결정
    if is_red:
        # 현재 빨간색이면 -> 다음은 초록색으로 변경
        new_color = "green"
    else:
        # 현재 초록색이면 -> 다음은 빨간색으로 변경
        new_color = "red"
    
    # 2. canvas.itemconfig()를 사용하여 원의 fill 속성을 변경
    canvas.itemconfig(circle_id, fill=new_color)
    
    # 3. 상태 플래그를 반전시킵니다. (다음 클릭 시 다른 색상이 선택되도록)
    is_red = not is_red

# --- Tkinter 초기 설정 및 실행 ---
root = tk.Tk()
root.title("클릭으로 색상 토글")
root.geometry("400x300")

# Canvas 생성 및 원 그리기
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# 원을 그리고 ID를 저장 (초기 색상은 파란색이 아닌 초록색으로 설정합니다)
circle_id = canvas.create_oval(150, 100, 250, 200, fill="green", outline="black")

# 마우스 왼쪽 버튼 클릭 이벤트를 함수에 바인딩
canvas.bind("<Button-1>", toggle_color)

root.mainloop()
