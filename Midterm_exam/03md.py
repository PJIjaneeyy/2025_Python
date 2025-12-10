'''
문제 6. 접근자 / 설정자를 이용한 재고 관리 프로그램

다음 요구사항을 만족하는 프로그램을 작성하시오.
(※ 출력 문구나 줄바꿈은 동일하지 않아도 되며, 기능이 올바르면 정답으로 인정한다.)

[요구사항]
1. Inventory 클래스를 정의한다.
- 클래스 변수 stock 을 사용하여 전체 재고 수량을 관리한다.
- 생성자(__init__)는 "새 상품이 등록되었습니다." 문구를 출력한다.
- 접근자(getter) 와 설정자(setter) 를 구현한다.
- get_stock() : 현재 재고 수량을 반환한다.
- set_stock(amount) : 재고 수량을 직접 수정하되, 0 이상인 값만 허용한다.

2. 입고(add_stock) 와 출고(remove_stock) 메서드를 작성한다.
- add_stock(amount) : 0보다 큰 수량만 입고 가능
- remove_stock(amount) : 현재 재고보다 많은 수량은 출고 불가

3. 각각 실행 시 아래와 같은 문구를 출력한다.
10개가 입고되었습니다.
3개가 출고되었습니다.

4. 다음 코드를 실행했을 때 예시와 같은 출력이 나타나도록 하시오.

item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:", item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())
'''

class Inventory:
    stock = 0  # 클래스 변수 (모든 상품이 공유하는 재고 수량)

    def __init__(self):
        print("새 상품이 등록되었습니다.")

    # 접근자 (Getter)
    def get_stock(self):
        return Inventory.stock

    # 설정자 (Setter)
    def set_stock(self, amount):
        if amount >= 0:
            Inventory.stock = amount
        else:
            print("재고 수량은 음수가 될 수 없습니다.")

    # 입고 메서드
    def add_stock(self, amount):
        if amount > 0:
            Inventory.stock += amount
            print(f"{amount}개가 입고되었습니다.")
        else:
            print("0개 이하의 수량은 입고할 수 없습니다.")
        return Inventory.stock

    # 출고 메서드
    def remove_stock(self, amount):
        if 0 < amount <= Inventory.stock:
            Inventory.stock -= amount
            print(f"{amount}개가 출고되었습니다.")
        else:
            print("재고가 부족하거나 잘못된 수량입니다.")
        return Inventory.stock


# 실행 예시
item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:", item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())