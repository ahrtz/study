# 65 A 
# 90 z 155 77 
def solution(name):
    answer = 0
    for i in range(len(name)):
        if ord(name[i])>77:
            answer+=(91-ord(name[i]))
            answer+=i
        else:
            answer+=(ord(name[i])-65)
            answer+=i
    
    
    return answer