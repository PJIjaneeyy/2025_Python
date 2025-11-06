class Animal:
    def speak(Self):
        print("동물이 소리를 냅니다.")

class Dog:
    def __init__(self):
        self.animal = Animal()    # Has-a 관계(포함) -> 코드 구조: self.b = B()

    def speak(self):
        self.animal.speak()
        print("멍멍!")

dog = Dog()
dog.speak()