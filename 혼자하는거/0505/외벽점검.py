from itertools import permutations
def solution(n, weak, dist):
    answer = 0
    return answer

n=12
weak=	[1, 3, 4, 9, 10]
dist = [3, 5, 7]
# 거리 리스트 만들기 
distance_num=len(weak)
candidate = permutations(dist,len(dist))
for i in range(len(weak)):
    weak.append(weak[i]+n)

final_can=201
for can in candidate:
    # 후보 뽑기
    can=list(can)
    for i in range(distance_num+1): # 검사 위치 뽑기
        can_num=1
        tmp_weak=weak[i:i+distance_num]
        # 검사 위치 
        can1=can[:]
        examine_start=tmp_weak.pop(0)
        person_dist=can1.pop(0)
       
        while tmp_weak and can1:
            possible_dist=examine_start+person_dist
            if possible_dist>=tmp_weak[0]:
                for i in range(len(tmp_weak)-1,-1,-1):
                    if tmp_weak[i]<=possible_dist:
                        tmp_weak.pop(i)
                if not tmp_weak:
                    break
                else:
                    examine_start=tmp_weak.pop(0)
                    can_num+=1
                    person_dist=can1.pop(0)
            else:
                person_dist=can1.pop(0)
                examine_start=tmp_weak.pop(0)
                can_num+=1

        if not tmp_weak :
            if can_num< final_can:
                final_can=can_num
if final_can==201:
    final_can=-1
print(final_can)
# for i in candidate:
#     print(i)