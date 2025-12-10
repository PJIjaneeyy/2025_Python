class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def get_info(self):
        # 부모 클래스의 기본 정보 반환 (공통 기능)
        return f"이름: {self.name}, 번호: {self.id_number}"

class Student(Person):
    def __init__(self, name, student_id):
        # 부모 클래스의 생성자 호출 (is-a 관계의 초기화) [cite: 882, 957]
        super().__init__(name, student_id)

    def get_info(self):
        # 메소드 오버라이딩: 학생에 맞게 재정의 (다형성 구현) [cite: 991, 1184]
        return f"학생 이름: {self.name}, 학번: {self.id_number}"

# 객체 생성
student1 = Student("박제인", "20241237")

# 결과 출력 (다형적으로 오버라이딩된 메서드 호출)
print(student1.get_info())