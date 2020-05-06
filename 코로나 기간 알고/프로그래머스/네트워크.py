
    
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
def solution(n, computers):
    node=[0]*(n)
    a=1
    for i in range(len(computers)):
        connect(i,computers,a,node)
        a+=1

    answer = len(set(node))
    return answer
def connect(idx,computers,a,node):
    
    for i in range(len(computers)):
        if computers[idx][i]==1 and node[i]==0:
            node[i]=a

            if idx!=i:
                connect(i,computers,a,node)
print(solution(3,computers))