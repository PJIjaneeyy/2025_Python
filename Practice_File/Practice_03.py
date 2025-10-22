#도서 목록을 관리하는 BookShelf 클래스를 작성하세요.
#도서 제목 리스트 books를 속성으로 가지며,
#새 도서를 추가하는 add_book 메서드,
#현재 도서 개수를 반환하는 count_books 메서드를 구현
class BookShelf:
    # 1순위: 생성자 (빈 리스트로 초기화)
    def __init__(self):
        # 도서 제목을 저장할 리스트를 인스턴스 변수로 초기화
        self.books = [] 

    # 4순위: 일반 메서드 (도서 추가)
    def add_book(self, title):
        self.books.append(title)
        print(f"'{title}'이 서가에 추가되었습니다.")

    # 4순위: 일반 메서드 (도서 개수 반환)
    def count_books(self):
        # 리스트의 길이를 반환하여 도서 개수를 센다.
        return len(self.books)


# --- 객체 생성 및 실행 ---
my_shelf = BookShelf()

my_shelf.add_book("파이썬 코딩")
my_shelf.add_book("Tkinter 실습")
my_shelf.add_book("객체지향 이론")

print(f"현재 도서 목록: {my_shelf.books}")
print(f"총 도서 개수: {my_shelf.count_books()}권")