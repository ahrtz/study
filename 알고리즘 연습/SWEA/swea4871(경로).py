def find_route(s):
    global result
    visit[s]=1
    for i in range(1,V+1):
        if route[s][i]==1 and not visit[i]:
            if i == G:
                result=1
                return
            find_route(i)

test=int(input())
for i in range(test):
    V,E = map(int,input().split()) # V 노드개수 E 연결된거 표시
    route=[[0]*(V+1) for _ in range (V+1)]
    visit =[0]*(V+1)
    for _ in range(E):
        start_node,end_node = map(int,input().split())
        route[start_node][end_node] = 1
        
        # start_node,end_node = end_node,start_node
        # route[start_node-1][end_node-1] = 1
    S,G = map(int,input().split())
    result=0    
    find_route(S)
    print("#{} {}".format(i+1,result))
    

