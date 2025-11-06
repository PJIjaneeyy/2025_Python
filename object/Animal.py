class Animal(object):
    pass

class Dog(Animal):      
    def __init__(self,name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None       #나중에 쓸 수도 있다는 뜻. 값이 지금은 없지만 나중에 사용할 때 재정의해서 사용해줄 수 있음. (유연한 사용 가능)

dog1 = Dog("dog1")
person1 = Person("홍길동")
person1.pet = dog1