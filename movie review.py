class movie():
    title=['silnu oru kadal','ok ok','iruvar','intham oru vanam']
    director=['a','b','c','d']
    actor=['surya','Dulquar','prakashraj','asok']
    rev = []
    def __init__(self):
        for i in range(len(self.title)):
            print(self.title[i]," ",self.director[i]," ",self.actor[i])
    def review_count(self):
        for i in range(len(self.title)):
            print("ENTER YOUR REVIEW FOR",self.title[i],"MOVIE:1-10")
            act = int(input("ACT :"))
            dia = int(input("DIA :"))
            cinemo = int(input("CINEMO :"))
            editing = int(input("EDITING :"))
            soundtrack = int(input("SOUNDTRACK :"))
            self.rev.append(act+dia+cinemo+editing+soundtrack)
        print(self.rev)
    def recommend(self):
        for i in range(len(self.rev)):
            if self.rev[i]<10:
                print(self.title[i],"Not at All Recommended")
            elif 10<=self.rev[i]<25:
                print(self.title[i],"Average")
            elif 25<=self.rev[i]<35:
                print(self.title[i],"Watchable")
            elif 35<=self.rev[i]<45:
                print(self.title[i],"Recommended")
            else:
                print(self.title[i],"Highly Recommended")

if __name__ == "__main__":
    a=movie()
    a.review_count()
    a.recommend()

