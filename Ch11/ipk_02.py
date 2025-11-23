import tkinter as tk

class Pet:
    def __init__(self):
        pass

    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self):
        return "멍멍!"

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name, pet=None):
        self.name = name
        self.pet = pet

person = Person("홍길동")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("문제2")
        self.geometry("400x200")
        
        self.info_label = tk.Label(self, text="반려동물을 선택하고 '말하기'를 누르세요.", font=('Arial', 12))
        self.info_label.pack(pady=10)
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="강아지 선택", command=lambda: self.select_pet(Dog(), "강아지")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="고양이 선택", command=lambda: self.select_pet(Cat(), "고양이")).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="말하기", command=self.speak_pet).pack(side=tk.LEFT, padx=20)
        
        self.result_label = tk.Label(self, text="", font=('Arial', 12), fg='darkgreen')
        self.result_label.pack(pady=10)

    def select_pet(self, pet_obj, pet_name):
        person.pet = pet_obj
        self.info_label.config(text=f"{pet_name}를 선택했습니다.")
        self.result_label.config(text="")

    def speak_pet(self):
        if person.pet is None:
            self.result_label.config(text="먼저 반려동물을 선택하세요.")
            return

        speak_result = person.pet.speak() 
        
        output = f"{person.name}의 반려동물 → {speak_result}"
        self.result_label.config(text=output)

if __name__ == "__main__":
    app = App()
    app.mainloop()