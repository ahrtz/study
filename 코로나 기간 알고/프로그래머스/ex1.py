def solution(s):
    answer = True
    tmp=[]
    for i in s:
        if not tmp and i==')':
            answer=False
            break
        elif i=='(':
            tmp.append(i)
        elif i==')':
            if tmp[-1]=='(':
                tmp.pop()
    if tmp:
        answer=False
    return answer