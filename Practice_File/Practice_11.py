class Employee:
    empCount=0 #클래스 변수

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        Employee.empCount += 1 #새로운 객체 생성할 때마다 직원 수 증가

    def displayEmp(self):
        print(f"직원명: {self.name}, 월급: {self.salary}만원")

    def show_count(self):
        print(f"전체 직원 수: {Employee.empCount}명")

E1=Employee("제인", 300)
E2=Employee("민수", 280)

E1.displayEmp()
E2.displayEmp()

E1.show_count()
