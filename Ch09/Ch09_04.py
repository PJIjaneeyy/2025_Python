class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def raise_salary(self, amount):
        self.salary += amount
        print(f"{self.name}의 연봉이 {self.salary}으로 증가되었습니다.")

#이 밑에 보고 위에 클래스 완성해보기.

kim = Employee("kim", 5000)
lee = Employee("lee", 6000)

print(f"{kim.name}의 연봉은{kim.salary}입니다.")
print(f"{lee.name}의 연봉은 {lee.salary}입니다.")

kim.raise_salary(2000)
lee.raise_salary(2000)
