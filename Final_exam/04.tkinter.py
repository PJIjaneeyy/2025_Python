# [문제 4 변형] 과목 선택 프로그램 + clearCourses()만 Tkinter 연동
import tkinter as tk

# 1. 클래스 구조 (Person -> Student 상속, Student는 classes 리스트를 has-a)
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = [] # has-a 관계

    def clearCourses(self):
        # 원본 문제의 핵심 기능 중 하나: 과목 리스트 초기화
        self.classes = []
        return f"{self.name}의 과목이 모두 초기화되었습니다."

    def enrollCourses_manual(self, subjects):
        # 등록 기능은 GUI에서 처리하지만, 최종 리스트를 설정하는 메서드
        self.classes = subjects
        
        # 빈 리스트일 경우 예외 처리 (변형 추가)
        if not self.classes:
            return "현재 과목: 없음"
            
        return f"현재 과목: {', '.join(self.classes)}"

class App:
    def __init__(self, master):
        master.title("문제4 변형: 과목 초기화 기능 강조")
        master.geometry("380x280")

        self.student = Student("홍길동")
        self.subjects = ["Python", "AI", "DataScience"]
        self.check_vars = {} # 체크박스 상태를 저장할 딕셔너리

        # UI 구성
        tk.Label(master, text=f"학생: {self.student.name}", font=('Helvetica', 12, 'bold')).pack(pady=10)

        # Checkbutton 구성
        frame_checks = tk.Frame(master)
        frame_checks.pack(pady=5)
        for subject in self.subjects:
            var = tk.BooleanVar(value=False)
            self.check_vars[subject] = var
            tk.Checkbutton(frame_checks, text=subject, variable=var).pack(side=tk.LEFT, padx=10)

        # 버튼
        frame_buttons = tk.Frame(master)
        frame_buttons.pack(pady=15)
        
        tk.Button(frame_buttons, text="등록하기", command=self.register_courses, width=12).pack(side=tk.LEFT, padx=10)
        # clearCourses() 메서드와 연동 (시험 핵심)
        tk.Button(frame_buttons, text="초기화", command=self.reset_all, width=12).pack(side=tk.LEFT, padx=10) 

        self.result_label = tk.Label(master, text="과목을 선택하고 [등록하기]를 누르세요.", fg="blue")
        self.result_label.pack(pady=10)
    
    def register_courses(self):
        selected_courses = [
            subject for subject, var in self.check_vars.items() if var.get()
        ]
        
        # Student 객체의 has-a 속성(classes)에 등록
        result_msg = self.student.enrollCourses_manual(selected_courses)
        
        self.result_label.config(text=result_msg, fg="red")

    def reset_all(self):
        # 1. 클래스 메서드 호출: has-a 속성 초기화
        result_msg = self.student.clearCourses() 
        
        # 2. GUI 상태 초기화: 체크박스 해제
        for var in self.check_vars.values():
            var.set(False)

        self.result_label.config(text=result_msg, fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()