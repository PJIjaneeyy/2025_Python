class Dog:
    def __init__(self,name,age, breed):
        self.name=name
        self.age=age
        self.breed=breed
    
    def bark(self):
        print("멍멍!")

    def info(self):
        print(f"이름:{self.name}, 나이:{self.age}, 견종:{self.breed}")
 
    def is_puppy(self):
        if self.age<=2:
            print("아직 강아지입니다.")

dog1=Dog("초코",1,"푸들")

dog1.info()
dog1.bark()
dog1.is_puppy()


