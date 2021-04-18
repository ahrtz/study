# from itertools import permutations
import math
def solution(n, k):

    answer=[]
    num_list=[a for a in range(1,n+1)]
    # temp_list = (permutations(num_list,len(num_list)))
    # cnt=0
    # for i in temp_list:
    #     cnt+=1
    #     if cnt==k:
    #         answer=i
    while n!=0:
        temp = math.factorial(n)// n  # 개수
        idx = k //temp     # 몇번째 앞자리
        k = k % temp # 뒷순번
        if k==0:
            answer.append(num_list.pop(idx-1))
        else:
            answer.append(num_list.pop(idx))
        n-=1


    print(answer)
    return answer


solution(3,5)