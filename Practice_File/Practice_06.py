class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name

    def show_info(self):
        print(f"학번:{self.stu_id}, 이름:{self.name}")

s1=DSstudent("20241237","박제인")
s2=DSstudent("20241238","홍길동")

s1.show_info()
s2.show_info()
        