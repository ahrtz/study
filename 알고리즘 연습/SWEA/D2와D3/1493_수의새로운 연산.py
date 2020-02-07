import pprint
T=int(input())
for tc in range(T):
    a,b=map(int,input().split())
    pan = [[0]*1000 for _ in range(1000)]
    tmp=1
    # 절반까지 밖에 못채우겟어서 야매로 10000개가 절반안에 들어오는판 생성
    while True:
        for k in range(1000):
            for l in range(0,k+1):
                pan[k-l][l] = tmp
                tmp+=1
        
        break
    
    #a 와 b의 인덱스 뽑기
    for i in range(len(pan)):
        try:
            pan[i].index(a)
            ar,ac = i,pan[i].index(a)
        except :
            pass
    for l in range(len(pan)):
        try:
            pan[l].index(b)
            br,bc=l,pan[l].index(b)
        except :
            pass

    print("#{} {}".format(tc+1,pan[ar+br+1][ac+bc+1]))