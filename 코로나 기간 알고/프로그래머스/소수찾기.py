from itertools import permutations
def solution(numbers):
    a=9999999
    m=int(a**0.5)
    can=[True]*(a+1)
    for i in range(2,m+1):
        if can[i]==True:
            
            for k in range(i+i,a+1,i):
                can[k]=False
    can[0]=False
    can[1]=False                
    # 소수 구해놓기



    num_list=list(numbers)
    answer1=[]
    answer = 0
    for k in set(num_list):
        answer1.append(int(k))
    for i in range(2,len(num_list)+1):
        for k in set(permutations(num_list,i)):
            answer1.append(int("".join(k)))
    for l in set(answer1):
        if can[l]==True:
            answer+=1
    
    # print(set(answer1))
    return answer
numbers='17'
print(solution(numbers))