import random

team1 = ["손초능",'김현준','김현성','이영인','김장후']
team2 = ['강찬엽','성근제','조범규']
team3 = ['조재빈','이동혁','김보훈','박성빈']
team4 = ['김재영','김선민','박준성']

male = [*team1,*team2,*team3,*team4]


female = ['제유빈','최예원','정아린','유세정','박지윤','박하은','권경은']





nteam1=[]
nteam2=[]
nteam3=[]
nteam4=[]
nteam5=[]

nteam1.append(male.pop(random.randrange(len(male))))
nteam1.append(male.pop(random.randrange(len(male))))
nteam1.append(male.pop(random.randrange(len(male))))
nteam1.append(female.pop(random.randrange(len(female))))
nteam1.append(female.pop(random.randrange(len(female))))


nteam2.append(male.pop(random.randrange(len(male))))
nteam2.append(male.pop(random.randrange(len(male))))
nteam2.append(male.pop(random.randrange(len(male))))
nteam2.append(female.pop(random.randrange(len(female))))
nteam2.append(female.pop(random.randrange(len(female))))

nteam3.append(male.pop(random.randrange(len(male))))
nteam3.append(male.pop(random.randrange(len(male))))
nteam3.append(male.pop(random.randrange(len(male))))
nteam3.append(female.pop(random.randrange(len(female))))


nteam4.append(male.pop(random.randrange(len(male))))
nteam4.append(male.pop(random.randrange(len(male))))
nteam4.append(male.pop(random.randrange(len(male))))
nteam4.append(female.pop(random.randrange(len(female))))

nteam5.append(male.pop(random.randrange(len(male))))
nteam5.append(male.pop(random.randrange(len(male))))
nteam5.append(male.pop(random.randrange(len(male))))
nteam5.append(female.pop(random.randrange(len(female))))




print(nteam1)
print(nteam2)
print(nteam3)
print(nteam4)
print(nteam5)

#['박성빈', '강찬엽', '이영인', '박하은', '최예원']
# ['성근제', '김선민', '손초능', '유세정', '제유빈']
# ['김현성', '조재빈', '김장후', '박지윤']
# ['이동혁', '김현준', '김보훈', '권경은']
# ['조범규', '박준성', '김재영', '정아린']
