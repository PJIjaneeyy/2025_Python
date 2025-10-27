#상품을 나타내는 Product 클래스를 작성하세요.
#상품명 name과 가격 __price를 속성으로 가지며,
#가격은 정보 은닉을 적용합니다.
#가격을 변경하는 Setter set_price를 구현하여
#가격이 음수가 되는 것을 방지
class Product:
    # 1순위: 생성자 
    def __init__(self, name, price):
        self.name = name
        self.__price = 0          # 정보 은닉 적용된 가격 변수 초기화
        self.set_price(price)     # Setter를 통해 초기값 설정 (유효성 검사 포함)

    # 3순위: 접근자 (Getter)
    def get_price(self):
        return self.__price

    # 2순위: 설정자 (Setter) - 유효성 검사 로직 포함
    def set_price(self, new_price):
        # 가격이 0 이상인지 검사
        if new_price >= 0:
            self.__price = new_price
            print(f"가격이 {new_price}원으로 설정되었습니다.")
        else:
            print("가격 오류: 가격은 음수가 될 수 없습니다.")


p1 = Product("Laptop", 1200000)

print(f"상품명: {p1.name}, 현재 가격: {p1.get_price()}원")

p1.set_price(-50000) # 유효하지 않은 값 시도
p1.set_price(1500000) # 유효한 값 시도

print(f"변경 후 가격: {p1.get_price()}원")
