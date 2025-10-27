#직원을 나타내는 Employee 클래스를 작성하세요.
#모든 객체가 공유하는 **클래스 변수 total_employees
#를 사용하여 생성된 총 직원 수를 관리하고, 직원의 이름,
#직급을 초기화합니다. 직원 정보를 출력하는 메서드 display_info를 완성

class Employee:
    # 0순위: 클래스 변수 정의 (모든 객체가 공유)
    total_employees = 0 

    # 1순위: 생성자 (객체 상태 초기화 및 클래스 변수 업데이트)
    def __init__(self, name, position):
        self.name = name          # 인스턴스 변수
        self.position = position  # 인스턴스 변수
        # 클래스 변수 업데이트 (클래스 이름으로 접근)
        Employee.total_employees += 1  

    # 4순위: 일반 메서드 (정보 출력)
    def display_info(self):
        print(f"이름: {self.name}, 직급: {self.position}")

# --- 객체 생성 및 실행 ---
# 생성자: Employee("이름", "직급")
emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Developer")

emp1.display_info()
emp2.display_info()

# 클래스 변수 확인: 클래스 이름으로 접근
print(f"\n총 직원 수: {Employee.total_employees}명")
