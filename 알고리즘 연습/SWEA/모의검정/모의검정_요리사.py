import itertools
T=int(input())
for tc in range(T):
    N= int(input())
    ingre = []
    for _ in range(N):
        ingre.append(list(map(int,input().split())))
    a=list(range(N))
    a_li=(list(itertools.combinations(a,N//2)))

    b_li=[]



    # 요게 재료 4개 
    for i in range(len(a_li)):
        tmp=a[:]
        tmp1=[]
        for k in range(N//2):
            tmp.remove(a_li[i][k])
            # print(tmp)
        b_li.append(tmp)
    score = []
    

    if len(a_li[0])!=2:
        a__li=[]
        b__li=[]
        for num in range(len(a_li)):
            a__li.append(list(itertools.combinations(a_li[num],2)))
            b__li.append(list(itertools.combinations(b_li[num],2)))

        for firstt in range(len(a__li)):
            a_score = 0
            b_score = 0
            for times in range(len(a__li[0])):
                
                for sec in range(2): # 원래는 n//2
                    a_score += ingre[a__li[firstt][times][sec]-1][a__li[firstt][times][1-sec]-1]
                    b_score += ingre[b__li[firstt][times][sec]-1][b__li[firstt][times][1-sec]-1]
            score.append(abs(a_score-b_score))    
        print("#{} {}".format(tc+1,min(score)))





    else:
        for first in range(len(a_li)):
            a_score=0
            b_score=0
            for sec in range(2):
                a_score += ingre[a_li[first][sec]-1][a_li[first][1-sec]-1]
                b_score += ingre[b_li[first][sec]-1][b_li[first][1-sec]-1]
            score.append(abs(a_score-b_score))
        print("#{} {}".format(tc+1,min(score)))