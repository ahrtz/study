def solutions(S):
    answer=[]
    cnt=0
    while len(S)>1:
        tmp = S.pop(0)
        for k in range(len(S)):
            for i in range(len(tmp)):
            # tmp[i] # 문자열 1개 
                if S[k][i]==tmp[i]:
                    answer.append(cnt)
                    answer.append(cnt+k+1)
                    answer.append(i)
                    return answer
        cnt+=1
    return answer




S=['bdafg','ceagi']
print(solutions(S))