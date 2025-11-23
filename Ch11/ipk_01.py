import tkinter as tk

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        raise NotImplementedError

class Car(Vehicle):
    def drive(self):
        return f"승용차 {self.name}가 주행합니다."

class Truck(Vehicle):
    def drive(self):
        return f"트럭 {self.name}가 화물을 싣고 주행합니다."

car1 = Car("car1")
truck1 = Truck("truck1")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("문제1")
        self.geometry("400x300")
        
        tk.Label(self, text="버튼을 눌러보세요.", font=('Arial', 14)).pack(pady=20)
        
        self.result_label = tk.Label(self, text="", font=('Arial', 12), fg='blue')
        self.result_label.pack(pady=30)
        
        button_frame = tk.Frame(self)
        button_frame.pack()
        
        tk.Button(button_frame, text="자동차 주행", command=self.car_drive).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="트럭 주행", command=self.truck_drive).pack(side=tk.LEFT, padx=10)
        
    def car_drive(self):
        result = car1.drive()
        self.result_label.config(text=result)
        
    def truck_drive(self):
        result = truck1.drive()
        self.result_label.config(text=result)

if __name__ == "__main__":
    app = App()
    app.mainloop()