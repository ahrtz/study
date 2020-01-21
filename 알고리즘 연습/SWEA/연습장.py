T = int(input())
for i in range(T):
    K, N, M = map(int, input().split(' '))
    location = list(map(int, input().split(' ')))
    re_location = [*location, N]
    # print(re_location)
    interval = []
    for j in range(len(re_location)-1):
        interval.append(re_location[j+1]-re_location[j])
    interval = [re_location[0], *interval]
    print(interval)
    if max(interval) > K:
        result = 0
    else:
        result = 0
        dist = interval[0]
        
        for k in range(len(interval)-1):
            dist += interval[k+1]
            print(dist)
            if dist > K:
                result += 1
                dist=interval[k+1]
    print('#%d %d'%(i+1,result))