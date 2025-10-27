class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print(f"{self.owner} 계좌 생성 완료.")

    def deposit(self, amount):
        self.balance+=amount
        print(f"{amount}원 입급되었습니다. 현재 잔액:{self.balance}원")

    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액 부족")
        else:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액: {self.balance}원")

    def show_balance(self):
        return self.balance
    
u1=Account("제인",0)

u1.deposit(500)

u1.withdraw(200)

u1.show_balance()


