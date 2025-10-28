class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{self.owner} 계좌에 {amount}원이 입금되었습니다. 현재 잔액: {self.balance}원")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.owner} 잔액: {self.balance}원")
        else:
            print("잔액이 부족합니다.")

    def transfer(self, other, amount):
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
            print(f"{self.owner} 계좌에서 {other.owner} 계좌로 {amount}원 송금 완료.")
            print(f"{self.owner} 잔액: {self.balance}원 \n{other.owner} 잔액: {other.balance}원")
        else:
            print("송금 실패: 잔액이 부족합니다.")
            

user1=BankAccount("A", 1000)
user2=BankAccount("B", 1000)

user1.deposit(500)
user2.deposit(300)

user1.transfer(user2, 200)

