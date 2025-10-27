class Student:
    def __init__(self,name):
        self.name=name
        self.scores=[] #빈 리스트로 초기화 할 시 속성에서 제외하기.

    def add_score(self,score):
        self.scores.append(score)

    #평균 성적 반환: 반환은 return함수 쓰기
    def cal_avg(self):
        #0으로 나누는 에러 방지를 위해 조건 추가
        if len(self.scores)==0:
            return 0
        return sum(self.scores)/len(self.scores)
    
    def grade(self):
        avg = self.cal_avg() #직접 지정을 해줘야함.
#if다음 elif 문으로 연결해야지 여러 조건이 동시에 참이 되어 중복 출력되는 일이 없어짐.
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else:
            grade = "F"
#avg:.1f =평균을 소수점 첫째 자리까지만 출력
        print(f"학생 이름:{self.name}, 평균:{avg:.1f}, 학점:{grade}")

s1=Student("제인")

s1.add_score(90)
s1.add_score(85)
s1.add_score(95) #add는 값을 줘야함.

s1.cal_avg()
s1.grade()


