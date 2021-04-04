def search(res):
    global cnt
    try:
        cnt+= len(child[res])
    except:
        pass
    for i in child[res]:
        search(i)



T=int(input())
for tc in range(T):
    V,E,target_A,target_B=map(int,input().split())
    child={i:[] for i in range(1,V+1)}
    parent={}
    nodelist=list(map(int,input().split()))
    for i in range(len(nodelist)//2):
        parent_node = nodelist[2*i]
        child_node = nodelist[2*i+1]
        child[parent_node].append(child_node)
        parent[child_node]=parent_node
    parent_A=[]
    print(child)
    tmp=target_A
    while True:
        try:
            parent_A.append(parent[tmp])
        except :
            break
        tmp=parent[tmp]
    parent_b=parent[target_B]
    while parent_b not in parent_A:
        parent_b=parent[parent_b]
    # print(parent_b)# 이게 겹치는 부모 노드 
    cnt=1
    # print(child)
    # 최상위 부모 노드의 자식들 
    # print(len(child[parent_b]))
    search(parent_b)
    # print(cnt)
    print(f'#{tc+1} {parent_b} {cnt}')