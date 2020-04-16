def number(nodex):
    global N
    if node[nodex]==0:
        # 분기 자식이 두개잇나 한개잇나 
        if nodex*2==N:
            node[nodex]=number(nodex*2)
        else:
            node[nodex]=number(nodex*2)+number(nodex*2+1)

    return node[nodex]
    


T=int(input())
for tc in range(T):
    N,M,L = map(int,input().split())
    node = [0]*(N+1)
    for _ in range(M):
        idx,val = map(int,input().split())
        node[idx]=val
    # print(node)
    a=number(L)
    print("#{} {}".format(tc+1,a))