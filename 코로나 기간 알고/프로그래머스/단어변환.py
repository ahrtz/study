begin = 'hit'
target= 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    startq = [begin]
    
    while startq:
        for start in startq:
            tmp=[]
            for word in words:
                
                cnt=0
                for i in range(len(word)):
                    if start[i]!=word[i]:
                        cnt+=1
                    if cnt==2:
                        break
                if cnt ==1:
                    tmp.append(word)
                    words.remove(word)
        # print(tmp)
        answer+=1
        if target in tmp:
            return answer
        else:
            startq=tmp
    return 0
print(solution(begin,target,words))