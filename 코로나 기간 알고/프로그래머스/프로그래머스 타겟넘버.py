# a=['+','-']
# b=[a,a]
# # print(b)
# i=3
# print(list(itertools.product(a,repeat=i)))

from itertools import product 
numbers=[1, 1, 1, 1, 1]
target=3
def solution(numbers, target):
    gil=len(numbers)
    a=["+",'-']
    # 부호 리스트 
    buho_list = list(product(a,repeat=(gil)))
    answer=0
    for m in buho_list:
        
        tmp=0
        
        for i in range(gil):
            if m[i]=='+':
                tmp+=numbers[i]
                
            else:
                tmp-=numbers[i]
        if tmp == target:
            
            answer+=1
    return answer
print(solution(numbers,target))