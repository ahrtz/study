T=int(input())
for tc in range(T):
    container,truck = map(int,input().split())
    화물_무게 = list(map(int,input().split()))
    트럭_용량 = list(map(int,input().split()))
    화물_무게=sorted(화물_무게,reverse=True)
    트럭_용량 = sorted(트럭_용량,reverse=True)
    tmp=[0]*len(트럭_용량)
    for i in range(len(트럭_용량)):
        for j in range(len(화물_무게)):
            if 트럭_용량[i]>=화물_무게[j]:
                tmp[i]=화물_무게.pop(j)
                
                break

    print(f"#{tc+1} {sum(tmp)}")