T= int(input())
for tc in range(T):
    N= int(input())
    pan = [list(map(int,input().split())) for _ in range(N)]
    d=((1,1),(-1,1),(1,-1),(-1,-1))
    cnt=0
    for r in range(1,N-1):
        for c in range(N-1):
            dessert = []
            spr,spc =r,c
            while True:
                for i in range(4):
#try except 쓰면 될것같은데 술먹엇으니 내일 
# 방향을 픽스하고 돌리기 try except 로 조건 충족하면 돌리기 
#visited 를 set 으로 만들거나 cnt 에 +1 하기 