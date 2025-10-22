#키보드 엔터키 입력으로 텍스트 동적 변경
import tkinter as tk

# 전역 위젯 변수
entry_input = None
status_label = None

def update_label(event):
    # 1. Entry 위젯에서 현재 입력된 문자열을 가져옵니다.
    new_text = entry_input.get()
    
    # 2. Label 위젯의 텍스트 속성을 가져온 문자열로 변경합니다.
    # configure() 또는 속성 접근(status_label['text']) 사용
    status_label.config(text=f"입력된 내용: {new_text}")
    
    # 3. (선택 사항) 입력 필드를 비웁니다.
    entry_input.delete(0, tk.END)


# --- Tkinter 초기 설정 및 실행 ---
root = tk.Tk()
root.title("Enter로 레이블 변경")
root.geometry("300x150")

# 1. Entry 위젯 생성 및 바인딩
input_label = tk.Label(root, text="텍스트 입력 후 Enter:")
input_label.pack(pady=5)

entry_input = tk.Entry(root, width=30)
entry_input.pack()

# <Return> 이벤트(엔터 키)를 update_label 함수에 바인딩
entry_input.bind("<Return>", update_label)

# 2. 결과 출력 Label 생성
status_label = tk.Label(root, text="여기에 입력 내용이 표시됩니다.", fg="blue")
status_label.pack(pady=15)

root.mainloop()