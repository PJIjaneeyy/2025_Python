import tkinter as tk

class Pet:
    def __init__(self, name):
        self.name = name
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
        self.title("문제 5")
        self.geometry("700x300")
        
        tk.Label(self, text="반려동물 등록하기", font=('Arial', 16, 'bold')).pack(pady=10)
        
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="반려동물 이름:").pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.pack(side=tk.LEFT, padx=10)
        
        self.pet_type_var = tk.StringVar(value="Dog")
        tk.Label(self, text="종류:").pack(anchor=tk.W, padx=20)
        type_frame = tk.Frame(self)
        type_frame.pack(anchor=tk.W, padx=20)
        tk.Radiobutton(type_frame, text="강아지", variable=self.pet_type_var, value="Dog").pack(side=tk.LEFT)
        tk.Radiobutton(type_frame, text="고양이", variable=self.pet_type_var, value="Cat").pack(side=tk.LEFT)

        tk.Label(self, text="옵션:").pack(anchor=tk.W, padx=20)
        option_frame = tk.Frame(self)
        option_frame.pack(anchor=tk.W, padx=20)
        
        self.vaccine_var = tk.IntVar()
        self.neuter_var = tk.IntVar()
        tk.Checkbutton(option_frame, text="예방접종 완료", variable=self.vaccine_var).pack(side=tk.LEFT)
        tk.Checkbutton(option_frame, text="중성화 완료", variable=self.neuter_var).pack(side=tk.LEFT, padx=10)
        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=15)
        
        tk.Button(button_frame, text="등록하기", command=self.register_pet).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="초기화", command=self.clear_form).pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self, text="", font=('Arial', 11), justify=tk.LEFT)
        self.result_label.pack(pady=10)

    def register_pet(self):
        pet_name = self.name_entry.get().strip()
        pet_type = self.pet_type_var.get()
        is_vaccine = self.vaccine_var.get()
        is_neuter = self.neuter_var.get()

        if not pet_name:
            pet_name = "이름없음"
        
        if pet_type == "Dog":
            new_pet = Dog(pet_name)
            type_korean = "강아지"
        else:
            new_pet = Cat(pet_name)
            type_korean = "고양이"
            
        person.pet = new_pet

        result_text = f"{person.name}의 반려동물 등록 완료!\n" \
                      f" 이름: {new_pet.name} ({type_korean})\n" \
                      f" 소리: {new_pet.speak()}!\n" \
                      f" 예방접종: {'O' if is_vaccine else 'X'}, 중성화: {'O' if is_neuter else 'X'}"
                      
        self.result_label.config(text=result_text, fg='darkblue')

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.pet_type_var.set("Dog")
        self.vaccine_var.set(0)
        self.neuter_var.set(0)
        self.result_label.config(text="모든 항목을 초기화했습니다.", fg='black')

if __name__ == "__main__":
    app = App()
    app.mainloop()