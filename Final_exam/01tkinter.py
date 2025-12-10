# [문제 1 변형] Vehicle 계층과 다형적 get_description() + Tkinter
import tkinter as tk

# 1. 클래스 정의
class Vehicle:
    def __init__(self, name):
        self.name = name

    # 추상 메서드 역할 (자식 클래스에서 반드시 오버라이드해야 함)
    def get_description(self):
        raise NotImplementedError("하위 클래스에서 이 메서드를 구현해야 합니다.")

class Car(Vehicle):
    def get_description(self):
        # 다형성 구현 1: Car의 정보 반환
        return f"차종: 승용차, 모델: {self.name}"

class Truck(Vehicle):
    CARGO_CAPACITY = "5톤" # Truck만의 새로운 속성 (상수로 표현)

    def get_description(self):
        # 다형성 구현 2: Truck의 정보 반환
        return f"차종: 트럭, 모델: {self.name}, 적재량: {self.CARGO_CAPACITY}"

class App:
    def __init__(self, master):
        master.title("문제1 변형: 차량 정보 다형성")
        master.geometry("400x300")

        # 3. 객체 생성 (전역 변수로 접근 가능하도록 인스턴스 변수로 저장)
        self.car = Car("Sonata")
        self.truck = Truck("Cargo99")

        # UI 구성
        tk.Label(master, text="차량 정보를 확인해 보세요.", pady=10).pack()

        tk.Button(master, text="승용차 정보", command=self.display_car_info, width=15).pack(pady=5)
        tk.Button(master, text="트럭 정보", command=self.display_truck_info, width=15).pack(pady=5)

        self.result_label = tk.Label(master, text="버튼을 눌러 결과를 확인하세요.", fg="blue", pady=20)
        self.result_label.pack()

    def display_car_info(self):
        # 다형적 호출: drive() 대신 get_description() 사용
        result = self.car.get_description()
        self.result_label.config(text=result)

    def display_truck_info(self):
        # 다형적 호출
        result = self.truck.get_description()
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()