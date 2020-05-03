# scovile =[1,2,3,9,10,12]

# def solution(scoville, K):
#     answer = 0
#     while len(scoville)>1:
#         tmp1=min(scoville)
#         scoville.remove(tmp1)
#         tmp2=min(scoville)
#         scoville.remove(tmp2)
#         tmp3 = tmp1+tmp2*2
#         scoville.append(tmp3)
        
#         answer+=1
#         if min(scoville)>=K:
#             break
#     if len(scoville)==1:
#         if scoville[0]<K:
#             return -1
#         else:
#             return answer
#     else:
#         return answer
# print(solution(scovile,7))
import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
        else:
            return -1
    return answer