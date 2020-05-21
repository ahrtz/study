def solution(tickets):
    start_idx=[]
    # tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    for sp in tickets:
        if sp[0]=='ICN':
            start_idx.append(sp)
    ans=[]
    def bfs(start,alist):
        print(start[1],alist)
        if len(tmp)==len(alist):
            ans.append(tmp)
            return
        for i in range(len(alist)):
            # alist=sorted(alist,key=lambda x: (x[0],x[1]))
            if start[1]==alist[i][0] and visited[i]==0:
                tmp.append(alist[i])
                visited[i]=1
                bfs(alist[i],alist)
                

    for i in start_idx:
        tmp=[]
        tmp_list = tickets[:]
        visited=[0]*(len(tickets)-1)
        tmp_list.remove(i)
        bfs(i,tmp_list)
        # print(i)
    tmp_ans=[]
    for k in range(len(ans)):
        tmpp=['ICN']
        for i in range(len(ans[k])):
            tmpp.append(ans[k][i][0])
        tmpp.append(ans[k][-1][-1])
        tmp_ans.append(tmpp)
    print(tmp_ans)


    return sorted(tmp_ans, key=lambda x: (x[0], x[1]))[0]
# tickets = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
tickets = [ ["ICN", "COO" ], [ "COO", "ICN"],[ "COO", "ICN"] ]
print(solution(tickets))