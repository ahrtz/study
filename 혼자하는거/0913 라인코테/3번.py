answer=0
min_cnt=2**32
def solution(n):
    num=str(n)
    num_len=len(num)
    cnt=0
    if num_len==1:
        return [cnt,n]
    for i in range(1,num_len):
        plus(num[:i],num[i:],cnt)
    return [min_cnt,answer]


def plus(num1,num2,cnt):
    global min_cnt,answer
    cnt+=1
    if cnt>min_cnt:
        return
    if num1[0]=='0' or num2[0]=='0':
        return 
    res=int(num1)+int(num2)
    res1=str(res)
    print(res,cnt,'#')
    if len(res1)==1:
        if cnt<min_cnt:
            min_cnt=cnt
            answer=res
    else:
        for i in range(1,len(res1)):
            plus(res1[:i],res1[i:],cnt)
print(solution(73425))
