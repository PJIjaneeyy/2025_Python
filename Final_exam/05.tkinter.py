# [문제 5 변형] 반려동물 등록 프로그램 + 추가 옵션 상태 출력
import tkinter as tk

# 1. 클래스 정의 (is-a 관계)
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

# Person 클래스는 Pet 객체를 속성으로 가짐 (has-a 관계)
class Person:
    def __init__(self, name):
        self.name = name
        self.pet = None 

class App:
    def __init__(self, master):
        master.title("문제5 변형: 옵션 상태 출력")
        master.geometry("700x350")
        
        self.person = Person("홍길동")
        
        # 입력 변수
        self.pet_name_var = tk.StringVar(value="")
        self.pet_type_var = tk.StringVar(value="Dog") # 기본값 강아지
        self.check_vac_var = tk.BooleanVar(value=False)
        self.check_train_var = tk.BooleanVar(value=False) # 중성화 -> 훈련으로 변경 (변형 요소)

        # UI 구성
        tk.Label(master, text="반려동물 등록하기", font=('Helvetica', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

        # 펫 이름 입력
        tk.Label(master, text="반려동물 이름:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
        tk.Entry(master, textvariable=self.pet_name_var, width=30).grid(row=1, column=1, sticky='w', padx=10, pady=5)

        # 종류 선택 (Radiobutton)
        tk.Label(master, text="종류:").grid(row=2, column=0, sticky='w', padx=10, pady=5)
        frame_type = tk.Frame(master)
        frame_type.grid(row=2, column=1, sticky='w', padx=10, pady=5)
        tk.Radiobutton(frame_type, text="강아지", variable=self.pet_type_var, value="Dog").pack(side=tk.LEFT)
        tk.Radiobutton(frame_type, text="고양이", variable=self.pet_type_var, value="Cat").pack(side=tk.LEFT)

        # 옵션 선택 (Checkbutton)
        tk.Label(master, text="옵션:").grid(row=3, column=0, sticky='w', padx=10, pady=5)
        frame_options = tk.Frame(master)
        frame_options.grid(row=3, column=1, sticky='w', padx=10, pady=5)
        tk.Checkbutton(frame_options, text="예방접종 완료", variable=self.check_vac_var).pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(frame_options, text="훈련 완료", variable=self.check_train_var).pack(side=tk.LEFT, padx=5) # 변형 옵션

        # 버튼
        frame_buttons = tk.Frame(master)
        frame_buttons.grid(row=4, column=0, columnspan=2, pady=15)
        tk.Button(frame_buttons, text="등록하기", command=self.register_pet, width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_buttons, text="초기화", command=self.reset_all, width=15).pack(side=tk.LEFT, padx=10)

        # 결과 라벨 (Row 5~10)
        self.result_label1 = tk.Label(master, text="", justify=tk.LEFT, anchor='w')
        self.result_label1.grid(row=5, column=0, columnspan=2, sticky='w', padx=10)
        self.result_label2 = tk.Label(master, text="", justify=tk.LEFT, anchor='w')
        self.result_label2.grid(row=6, column=0, columnspan=2, sticky='w', padx=10)
        self.result_label3 = tk.Label(master, text="", justify=tk.LEFT, anchor='w')
        self.result_label3.grid(row=7, column=0, columnspan=2, sticky='w', padx=10)
        self.result_label4 = tk.Label(master, text="", justify=tk.LEFT, anchor='w')
        self.result_label4.grid(row=8, column=0, columnspan=2, sticky='w', padx=10)

        self.reset_labels() # 초기 문구 설정

    def reset_labels(self):
        # 초기 상태로 라벨 설정
        default_text = "반려동물 이름과 종류를 선택하고 등록해주세요."
        self.result_label1.config(text=default_text)
        self.result_label2.config(text="")
        self.result_label3.config(text="")
        self.result_label4.config(text="")

    def register_pet(self):
        pet_name = self.pet_name_var.get().strip()
        pet_type = self.pet_type_var.get()
        
        # 이름이 비어 있으면 "이름없음"으로 처리 (원본 문제 요구사항)
        if not pet_name: pet_name = "이름없음"

        # 종류에 따라 Dog 또는 Cat 객체 생성 (다형성)
        if pet_type == "Dog":
            new_pet = Dog(pet_name)
            pet_type_kr = "강아지"
        else: # Cat
            new_pet = Cat(pet_name)
            pet_type_kr = "고양이"
        
        self.person.pet = new_pet # Person 객체에 할당 (has-a)

        # 옵션 상태 확인
        vaccinated = "O" if self.check_vac_var.get() else "X"
        trained = "O" if self.check_train_var.get() else "X" # 변형된 옵션

        # 결과 출력 (원본 문제의 화면 형식 따름)
        self.result_label1.config(text=f"{self.person.name}의 반려동물 등록 완료!", fg="blue")
        self.result_label2.config(text=f" 이름: {new_pet.name} ({pet_type_kr})")
        self.result_label3.config(text=f" 소리: {new_pet.speak()}") # 다형적 호출
        self.result_label4.config(text=f" 예방접종: {vaccinated}, 훈련: {trained}", fg="darkgreen") # 변형된 옵션 출력

    def reset_all(self):
        # 모든 선택과 입력 초기화
        self.pet_name_var.set("")
        self.pet_type_var.set("Dog")
        self.check_vac_var.set(False)
        self.check_train_var.set(False)
        self.person.pet = None
        self.reset_labels()
        
        self.result_label1.config(text="모든 선택과 입력이 초기화되었습니다.", fg="green")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()