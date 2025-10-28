class BankAccount(object):
    interest_rate=0.3  #클래스 변수

    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance #인스턴스 변수

    def deposit(self, amount): #입금
        # 2. 잔고를 증가시키는 메서드
        self.balance += amount
        print("입금 성공")
        
    def withdraw(self, amount): #출금
        # 3. 잔고를 감소시키는 메서드 (잔액 부족 처리)
        if self.balance >= amount :
            self.balance -= amount
            print("인출 성공")
        else:
            print("잔액이 부족합니다.")

user1 = BankAccount("chung", "1111111", 1000)
print("초기 잔고:", user1.balance)
user1.deposit(500)
print("저축 후 잔고:", user1.balance)
user1.withdraw(200)
print("입출 후 잔고:", user1.balance)
user1.withdraw(10000)