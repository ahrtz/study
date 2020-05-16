def solution(number, k):
    result= []  
    for i, num in enumerate(number):
        while len(result) > 0 and result[-1] < num and k > 0:
            # print(result)
            result.pop()
            k -= 1
        if k == 0:
            result += list(number[i:])# 뒤에 남은거 가져다가 붙이기 
            break
        result.append(num)
    # print(result)
    # k가 남았을 경우 
    result = result[:-k] if k > 0 else result
    answer = ''.join(result)
    return answer
print(solution('4177252841',4))           