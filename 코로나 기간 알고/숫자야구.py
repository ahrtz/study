from itertools import permutations 
def strike(q,a):
    num=0
    if q[0]==a[0]:
        num+=1
    if q[1]==a[1]:
        num+=1
    if q[2]==a[2]:
        num+=1
    return num

def ball(q,a):
    num=0
    if q[0]==a[1]or q[0]==a[2]:
        num+=1
    if q[1]==a[0] or q[1]==a[2]:
        num+=1
    if q[2]==a[0] or q[2]==a[1]:
        num+=1
    return num


def solution(baseball):
    tmp=list(map(str,range(1,10)))
    can=[]
    for num in list(permutations(tmp,3)):
        can.append("".join(num))
    for i in range(len(baseball)):# 한개 꺼내기
        ans_tmp=[]
        # print(can)
        for cand in can:
            # 숫자를 비교해서 스트라이크랑 볼을 찾자
            q = str(baseball[i][0])
            if strike(q,cand)==baseball[i][1] and ball(q,cand)==baseball[i][2]:
                    ans_tmp.append(cand)
        can=ans_tmp
    return(len(can))

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))