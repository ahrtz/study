from copy import deepcopy
import pprint
def solution(key,lock):
    res=0
    for i in range(len(lock)):
        for k in range(len(lock)):
            res+=lock[i][k]
    if res==len(lock)**2:
        return True


    pan = [[0]*(2*(len(key)-1)+len(lock)) for _ in range(2*(len(key)-1)+len(lock))]
    for i in range(len(lock)):
        for j in range(len(lock)):
            pan[len(key)-1+i][len(key)-1+j]=lock[i][j]
    # print(pan)
    key1=turn90(key)
    key2=turn90(key1)
    key3=turn90(key2)
    # key를 넣는거 
    for i in range(len(pan)-len(key)): # 이제 시작점 잡기
        for j in range(len(pan)-len(key)):
            tmpPan = deepcopy(pan)
            tmpPan1 = deepcopy(pan)
            tmpPan2 = deepcopy(pan)
            tmpPan3 = deepcopy(pan)
            for k in range(len(key)): # 열쇠 길이 만큼 tmp pan 을 합치기
                for l in range(len(key)):
                    tmpPan[i+k][j+l]+=key[k][l]
                    tmpPan1[i+k][j+l]+=key1[k][l]
                    tmpPan2[i+k][j+l]+=key2[k][l]
                    tmpPan3[i+k][j+l]+=key3[k][l]
        #     pprint.pprint(tmpPan2)
        #     print(i,j)
        # break
            if check(tmpPan,lock,key) or check(tmpPan1,lock,key) or check(tmpPan2,lock,key) or check(tmpPan3,lock,key):
                # pprint.pprint(tmpPan)
                # pprint.pprint(tmpPan1)
                # pprint.pprint(tmpPan2)
                # pprint.pprint(tmpPan3)

                return True
            
    # print('Rmx')
    return False


# 여긴 검증하는거 
def check(pan,lock,key):
    cnt =0
    flag=1
    for i in range(len(lock)):
        for j in range(len(lock)):
            if pan[len(key)-1+i][len(key)-1+j]==1:
                cnt+=1
            else:
                flag=2
                break
        if flag==2:
            break
    if cnt == len(lock)**2:
        return True
    else:
        return False    

key=[[0, 0, 0,0], [1, 0, 0,0], [0, 1, 1,0],[1,1,1,1]]
lock= [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	

## 돌리는 알고 
def turn90(key):
    key1=[[0]*len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            key1[i][len(key)-1-j]=key[j][i]
    return key1

print(solution(key,lock))
# key1=turn90(key)
# key2=turn90(key1)
# key3=turn90(key2)

# print(key,key1,key2,key3)



