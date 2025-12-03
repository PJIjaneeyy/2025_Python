import sys

def read_and_print_file():
    """파일 이름을 입력받아 내용을 읽고 출력하며, 파일이 없을 경우 예외 처리"""
    
    filename = input("텍스트 파일 이름을 입력하세요: ")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
            
    except FileNotFoundError:
        print(f"오류: 파일 '{filename}'을(를) 찾을 수 없습니다.", file=sys.stderr)
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}", file=sys.stderr)

if __name__ == "__main__":
    read_and_print_file()