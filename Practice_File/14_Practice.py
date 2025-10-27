class Movie:
    def __init__(self, title, genre, ratings):
        self.title=title
        self.genre=genre
        self.ratings=[]

    def add_rating(self, score):
        #self.new=self.ratings + score (->list+int는 불가능. append 사용하기)
        self.ratings.append(score) #평점 추가
    
    def get_avg_rating(self):
        #return self.new/int(self.new) (->self.new는 숫자가 아니고 리스트이므로 에러가 남.)
        if len(self.ratings)==0:
            return 0
        return sum(self.ratings)/len(self.ratings)
    
    def show_info(self):
        print(f"영화: {self.title} ({self.genre})\n평균 평점: {self.get_avg_rating():.1f}")
        #소수점 한 자리까지 출력

m1=Movie("인사이드 아웃 2","애니메이션",8.5)

m1.add_rating(8)
m1.add_rating(9)

m1.show_info()
