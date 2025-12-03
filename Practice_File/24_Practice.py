import sys

def merge_files(file1_name, file2_name, output_name):
    """두 파일을 병합하여 새 파일로 저장하는 함수"""
    
    input_files = [file1_name, file2_name]
    
    try:
        with open(output_name, 'w', encoding='utf-8') as outfile:
            print(f"'{output_name}' 파일 쓰기 시작...")
            
            for input_name in input_files:
                try:
                    with open(input_name, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write('\n') 
                        print(f"'{input_name}' 파일 내용을 병합했습니다.")
                        
                except FileNotFoundError:
                    print(f"경고: 입력 파일 '{input_name}'을(를) 찾을 수 없어 병합에서 제외합니다.", file=sys.stderr)
        
        print(f"✅ 파일 병합이 완료되어 '{output_name}'에 저장되었습니다.")

    except Exception as e:
        print(f"파일 병합 중 오류 발생: {e}", file=sys.stderr)


if __name__ == "__main__":
    merge_files('file1.txt', 'file2.txt', 'output.txt')