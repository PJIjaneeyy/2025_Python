class Car:
    def __init__(self, model, speed=0):#기본값을 속성에서 지정해도됨.
        self.model=model
        self.speed=speed
        print(f"모델: {self.model}")

    def accelerate(self, value):
        self.speed += value
        print(f"속도 증가! 현재 속도: {self.speed}km/h")

    def brake(self, value):
        self.speed -=value
        if self.speed<0:
            self.speed=0
        print(f"감속 후 속도: {self.speed}km/h")

    def show_speed(self):
        print(f"현재 속도: {self.speed}km/h")
                
c1=Car("소나타",0)
c1.show_speed()

c1.accelerate(50)

c1.brake(30)
