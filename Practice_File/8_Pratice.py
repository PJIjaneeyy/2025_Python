class Dog:
    def __init__(self, name, tricks):
        self.name=name
        self.tricks=tricks
    
    def add_trick(self,trick):
        #단일 문자열 trick을 리스트에 추가
        self.tricks.append(trick)

    def show_tricks(self):
        print(f"{self.name}의 장기 목록:{self.tricks}")

t1=Dog("초코",["앉기","굴러가기"])
t1.add_trick("손") #장기 추가

t1.show_tricks()


