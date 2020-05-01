from collections import Counter

clothes= [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
a=[]
for cloth in clothes:
    a.append(cloth[1])
an = Counter(a)
if len(an)==1:
    print( list(an.values())[0])
else:
    answer =1
    for i in list(an.values()):
        answer*=(i+1)
    print(answer-1)