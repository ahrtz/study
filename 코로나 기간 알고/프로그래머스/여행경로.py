from copy import deepcopy
def solution(tickets):
    start_idx=[]
    city=[]
    for i in tickets:
        a,b=i
        city.append(a)
        city.append(b)
    for sp in range(len(tickets)):
        visited=[0]*(len(tickets))
        if tickets[sp][0]=='ICN':
            visited[sp]=1
            start_idx.append([tickets[sp],visited])
    tmp=[]
    # print(start_idx)
    for _ in range(len(tickets)-1):            
        for _ in range(len(start_idx)):
            route1,visite = start_idx.pop(0)
            # print(route1,visite,'%')
            
            for i in range(len(tickets)):
                visited=deepcopy(visite)
                route=deepcopy(route1)
                # print(visited,'&^%')
                if tickets[i][0]==route[-1] and visited[i]==0:
                    route.append(tickets[i][1])
                    visited[i]=1
                    tmp.append([route,visited])
                    # route.pop()
                    # print(route,visited)
                        # print(tmp)
                elif visited.count(0)==1:
                    tmp.append([route,visited])
                    
        start_idx=tmp
    
    
    tmp1=[]
    for i in start_idx:
        tmp1.append((i[0],len(i[0])))
    # print(tmp1)

    return sorted(tmp1,key=lambda x: (-x[1],x[0]))[0][0]    


print(solution( [[ 'ICN', 'BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO' ], [ 'BOO', 'DOO' ],  ['DOO', 'BOO'],
[ 'BOO', 'ICN' ], [ 'COO', 'BOO' ]]))
#     for sp in start_idx:
#         for i in range(len(tickets)):
#             if sp[1]==tickets[i][0]:
#                 ans.append()


#     for i in start_idx:
#         tmp=[]
#         tmp_list = tickets[:]
#         visited=[0]*(len(tickets)-1)
#         tmp_list.remove(i)
#         bfs(i,tmp_list)
#         # print(i)
#     tmp_ans=[]
#     for k in range(len(ans)):
#         tmpp=['ICN']
#         for i in range(len(ans[k])):
#             tmpp.append(ans[k][i][0])
#         tmpp.append(ans[k][-1][-1])
#         tmp_ans.append(tmpp)
#     print(tmp_ans)


# tickets = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
# print(solution(tickets))