class Book:
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price

    def show_info(self):
        print(f"제목: {self.title}, 저자: {self.author}, 가격: {self.price}원")

    def discount(self, rate):
        new_price = self.price * (1-rate/100)
        print(f"{rate}% 할인된 가격: {int(new_price)}원")

b1=Book("파이썬 프로그래밍", "홍길동", 20000)
b1.show_info()
b1.discount(10)
