class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")

class Dog(Animal):      #is-a 관계(상속) -> 코드구조:class A(B)
    def speak(self):
        print("멍멍!")

dog = Dog()
dog.speak()