# [문제 2 변형] Person-Pet 관계 (has-a) + get_name() 추가
import tkinter as tk

# 1. 클래스 정의 (Pet에 get_name() 메서드 추가)
class Pet:
    def __init__(self, name="이름없음"):
        self.name = name

    def get_name(self):
        return self.name

    def speak(self):
        return "..."

class Dog(Pet):
    def speak(self, action="짓습니다"):
        return f"멍멍! ({action})" # 메서드에 인자 추가 (추가 변형)

class Cat(Pet):
    def speak(self):
        return "야옹!"

class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None # has-a 관계

    def set_pet(self, pet_obj):
        self.pet = pet_obj

class App:
    def __init__(self, master):
        master.title("문제2 변형: Pet 이름 활용")
        master.geometry("450x220")

        self.person = Person("홍길동") # Person 객체 생성
        self.result_var = tk.StringVar(value="반려동물을 선택하고 '말하기'를 누르세요.")
        
        # UI 구성
        tk.Label(master, text=f"사람: {self.person.name}", fg="gray").pack(pady=5)
        tk.Label(master, textvariable=self.result_var, pady=10).pack()

        frame_buttons = tk.Frame(master)
        frame_buttons.pack(pady=10)

        # Pet 이름 입력 받기 (추가된 요소)
        tk.Label(frame_buttons, text="Pet 이름:").pack(side=tk.LEFT)
        self.pet_name_entry = tk.Entry(frame_buttons, width=15)
        self.pet_name_entry.insert(0, "덕성이")
        self.pet_name_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(frame_buttons, text="강아지 선택", command=lambda: self.select_pet("Dog")).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="고양이 선택", command=lambda: self.select_pet("Cat")).pack(side=tk.LEFT, padx=5)
        tk.Button(master, text="말하기", command=self.make_pet_speak, width=15).pack()

    def select_pet(self, pet_type):
        pet_name = self.pet_name_entry.get()
        if not pet_name: pet_name = "이름없음"

        if pet_type == "Dog":
            self.person.set_pet(Dog(pet_name))
            msg = f"'{pet_name}'(강아지)를 선택했습니다."
        elif pet_type == "Cat":
            self.person.set_pet(Cat(pet_name))
            msg = f"'{pet_name}'(고양이)를 선택했습니다."
        
        self.result_var.set(msg)

    def make_pet_speak(self):
        if self.person.pet:
            # Pet 객체의 get_name() 메서드를 활용하여 출력 (변형)
            pet_name = self.person.pet.get_name() 
            sound = self.person.pet.speak() 
            
            # Dog 클래스에만 있는 인자 처리 (추가된 다형성 테스트)
            if isinstance(self.person.pet, Dog):
                sound = self.person.pet.speak(action="꼬리를 흔들며 짖습니다")

            self.result_var.set(f"{pet_name}의 소리 → {sound}")
        else:
            self.result_var.set("반려동물을 먼저 선택해 주세요.")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()