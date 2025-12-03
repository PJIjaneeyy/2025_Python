def count_string_in_file():
    """파일에서 특정 문자열의 출현 횟수를 세는 프로그램"""

    filename = input("텍스트 파일 이름을 입력하세요: ")
    search_string = input("검색 문자열을 입력하세요: ")
    
    count = 0

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
            count = content.count(search_string)
            
            print(f"'{search_string}'(은)는 파일 내에서 {count}번 나타납니다.")

    except FileNotFoundError:
        print(f"오류: 파일 '{filename}'을(를) 찾을 수 없습니다.")
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")

if __name__ == "__main__":
    count_string_in_file()