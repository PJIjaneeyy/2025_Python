class Dog:
    def __init__(self, name, age, tricks):
        self.name = name
        self.age = age
        # 1. 장기 목록을 리스트로 저장하는 인스턴스 변수
        self.tricks = tricks # ['뒹굴기', '달리기'] 등 리스트가 저장됨 [cite: 44, 47, 64]

    def bark(self):
        print(f"{self.name}가 짖고 있습니다.")

    def info(self):
        print(f"이름:{self.name}, 나이:{self.age}살")

    def show_tricks(self):
        # 2. 리스트 요소를 ", "로 연결하여 문자열로 변환
        tricks=','.join(self.tricks)
        print(f"{self.name}의 장기는 {tricks} 입니다")
        


dog1 = Dog("바둑이", 3,["뒹굴기","달리기"]) 
dog2 = Dog("멍멍이", 5,["먹기"])


dog1.show_tricks()
dog2.show_tricks()