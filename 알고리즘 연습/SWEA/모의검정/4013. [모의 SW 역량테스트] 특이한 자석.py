def turn(gear,dir):
    if dir == 1:
        a=gear.pop(len(gear)-1)
        gear.insert(0,a)
        return gear
    elif dir == -1:
        a=gear.pop(0)
        gear.append(a)
        return gear
        
# 오른쪽하고 닿는 번호 2 왼쪽이랑 닿는 번호 6
T=int(input())
for tc in range(T):
    time = int(input())
    gear=[]
    for _ in range (4):
        tmp = list(map(int,input().split()))
        gear.append(tmp)

    dirr=[1,-1]
    times=[]
    for t in range(time):
        times.append(list(map(int,input().split())))
#5,6,9
    for l in range(len(times)):
        if times[l][0]==1: # 1번기어일때 :  회전 오른쪽만 검사
            
            dirr.remove(times[l][1])
            dirr.append(times[l][1])
            if gear[0][2]!=gear[1][6]:# 2번회전
                
                a=dirr.pop(0)
                dirr.append(a)

                if gear[1][2]!=gear[2][6]:
                    
                    b=dirr.pop(0)
                    dirr.append(b)
                    if gear[2][2]!=gear[3][6]:
                        gear[3]=turn(gear[3],dirr[0])
                        
                    gear[2]=turn(gear[2],b)
                gear[1]=turn(gear[1],a)
            gear[0] = turn(gear[0],times[l][1])
        elif times[l][0]==2:
            
            dirr.remove(times[l][1])
            dirr.append(times[l][1])
            if gear[1][2]!=gear[2][6]:# 3번회전
                
                a=dirr.pop(0)
                dirr.append(a)
                if gear[2][2]!=gear[3][6]:
                    gear[3]=turn(gear[3],dirr[0])
                    
                gear[2]=turn(gear[2],a)
            dirr=[1,-1]
            dirr.remove(times[l][1])
            dirr.append(times[l][1])
            if gear[1][6]!=gear[0][2]:
                gear[0]=turn(gear[0],dirr[0])
                tmp=dirr.pop(0)
                dirr.append(tmp)

            gear[1] = turn(gear[1],times[l][1])
        elif times[l][0]==3:            #3번기어
            dirr.remove(times[l][1])
            dirr.append(times[l][1])
            if gear[2][2]!=gear[3][6]:# 4번 기어회전
                gear[3]=turn(gear[3],dirr[0])
                tmp=dirr.pop(0)
                dirr.append(tmp)
            
            dirr=[1,-1]
            dirr.remove(times[l][1])
            dirr.append(times[l][1])            
            
            if gear[2][6]!=gear[1][2]:# 2번기어
                
                a=dirr.pop(0)
                dirr.append(a)
                if gear[1][6]!=gear[0][2]:
                    gear[0]=turn(gear[0],dirr[0])
                    tmp=dirr.pop(0)
                    dirr.append(tmp)
                gear[1]=turn(gear[1],a)
            gear[2] = turn(gear[2],times[l][1])
        elif times[l][0]==4:
            
            dirr.remove(times[l][1])
            dirr.append(times[l][1])
            if gear[3][6]!=gear[2][2]:# 3번회전
                
                a=dirr.pop(0)
                dirr.append(a)
                if gear[2][6]!=gear[1][2]:
                    
                    b=dirr.pop(0)
                    dirr.append(b)
                    if gear[1][6]!=gear[0][2]:
                        gear[0]=turn(gear[0],dirr[0])
                        tmp=dirr.pop(0)
                        dirr.append(tmp)
                    gear[1]=turn(gear[1],b)
                gear[2]=turn(gear[2],a)
            gear[3] = turn(gear[3],times[l][1])
    cnt=0
    if gear[0][0]==1:
        cnt+=1
    if gear[1][0]==1:
        cnt+=2
    if gear[2][0]==1:
        cnt+=4
    if gear[3][0]==1:
        cnt+=8
    print("#{} {}".format(tc+1,cnt))