import tkinter as tk

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes = [] 

    def enrollCourse(self, subject):
        if subject not in self.classes:
            self.classes.append(subject)

    def clearCourses(self):
        self.classes = []

student = Student("홍길동")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("문제 4")
        self.geometry("380x280")
        
        tk.Label(self, text=f"학생: {student.name}", font=('Arial', 14)).pack(pady=10)
        
        self.subjects = ["Python", "AI", "DataScience"]
        self.check_vars = {}
        
        for subject in self.subjects:
            var = tk.IntVar()
            cb = tk.Checkbutton(self, text=subject, variable=var, font=('Arial', 12))
            cb.pack(anchor=tk.W, padx=20)
            self.check_vars[subject] = var

        self.info_label = tk.Label(self, text="과목을 선택하고 [등록하기]를 누르세요.", font=('Arial', 10), fg='gray')
        self.info_label.pack(pady=10)
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="등록하기", command=self.register_courses).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="초기화", command=self.clear_selection).pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self, text=f"등록된 과목: {', '.join(student.classes)}", font=('Arial', 10), fg='blue')
        self.result_label.pack()

    def register_courses(self):
        student.clearCourses() 
        selected_count = 0
        
        for subject, var in self.check_vars.items():
            if var.get() == 1:
                student.enrollCourse(subject)
                selected_count += 1
                
        if student.classes:
            result_text = f"등록된 과목: {', '.join(student.classes)}"
        else:
            result_text = "등록된 과목이 없습니다."
            
        self.result_label.config(text=result_text)
        self.info_label.config(text=f"{selected_count}개의 과목을 등록했습니다.")


    def clear_selection(self):
        for var in self.check_vars.values():
            var.set(0)
        
        student.clearCourses()
        
        self.info_label.config(text="모든 선택을 해제했습니다.")
        self.result_label.config(text="등록된 과목: ")

if __name__ == "__main__":
    app = App()
    app.mainloop()