class Library:

    books=[] #각 객체마다 따로 books 리스트를 갖는 구조(인스턴스 변수) 대신,
             #모든 객체가 공유하는 클래스 변수로 적어야함.

    def __init__(self):
        #클래스 변수이므로 초기화할 인스턴스 변수가 없음.
        pass

    def add_book(self,title):
        Library.books.append(title)
        print(f"책 추가 완료: {title}")

    def show_books(self):
        if Library.books:
            print(f"전체 책 목록: {Library.books}")

    def count_books(self):
        print(f"총 {len(Library.books)}권 보유 중")


#도서관 객체 여러 개를 만들어도 같은 목록을 공유
L1=Library()
L2=Library()

L1.add_book("파이썬의 정석")
L2.add_book("알고리즘 기초")

L1.show_books()
L2.count_books()
