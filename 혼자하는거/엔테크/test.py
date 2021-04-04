import heapq
def solution(operations):
    heap=[]
    maxheap=[]
    for i in operations:
        command,num = i.split(" ")
        # print(i,command,num)
        if command=="I":
            heapq.heappush(heap,int(num)) 
            heapq.heappush(maxheap,-int(num))
        else:
            if heap:
                if int(num)==1:
                    heap.pop(-1)
                    heapq.heappop(maxheap)
                    
                else:
                    (heapq.heappop(heap))
                    maxheap.pop(-1)
        
    
    
    if heap:
        answer = [-maxheap[0],heap[0]]
    else:
        answer=[0,0]
    
    
    return answer


# print(solution(["I 7","I 5","I -5","D -1"]))
a=["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]
print(solution(a))