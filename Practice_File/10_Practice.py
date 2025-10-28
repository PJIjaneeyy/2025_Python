class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def raise_salary(self,rate):
        return self.salary *(1+rate/100)
#show info() 안에서 raise_salary를 호출함. 그 함수가 rate를 필요로 하기 때문에
#show_info안에 rate값을 넣어주는거임.
    def show_info(self,rate):
        new_salary=self.raise_salary(rate)
        print(f"직원명:{self.name}, 인상된 연봉:{int(new_salary)}원")

E1=Employee("박제인",200000000)
E1.show_info(10)
