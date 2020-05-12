def dfs(start, tickets, result):
    if len(tickets) == 0:
        return result
    for i,ticket in enumerate(tickets):
        if start == ticket[0]:
            end = ticket[1]
            tickets.pop(i)
            result.append(end)
            print(result)
            temp = dfs(end,tickets, result)
            if len(temp)!=0:
                return temp
            result.pop(len(result)-1)
            
            tickets.insert(i,[start,end])

    return []        

def solution(tickets):
    tickets.sort()
    result = []
    start = "ICN"
    result.append(start)
    answer = dfs(start, tickets, result)

    return answer