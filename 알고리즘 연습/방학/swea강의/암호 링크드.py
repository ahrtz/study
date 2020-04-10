def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        pre = Head
        while pre.link != None:
            pre = pre.link
        pre.link = Node(data, None)
        
# 노드 삭제
def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link
# 가운데 노드로 삽입
def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
# 첫번째 노드 삽입
def addtoFirst(data):
    global Head
    Head = Node(data, Head)
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n
T = int(input())
for tc in range(T):
    N,M,K  = map(int,input().split())
    numbers = list(map(int,input().split()))
    
    Head = None
    addtoFirst(numbers[0])
    
    for node in numbers[1:]:
        addtoLast(node)
    # 맨 마지막 노드값 찾기
    pre=Head
    while pre.link !=None:
        pre=pre.link
    pre.link = Head
    # 헤드 처음부터
    pre = Head
    cnt=0
    flag = 0
    while flag!=K:
        cnt+=1
        if cnt == M:
            add(pre,pre.item+pre.link.item)
            flag+=1
            cnt=0
        pre=pre.link
    
    #테스트 출력
    pre=Head
    cnt = 0
    res=[0]*(N+K)
    while pre.link!=None:
        # print(pre.item,cnt)
        res[cnt]=pre.item
        pre=pre.link
        cnt+=1
        if cnt ==N+K:
            break
    if len(res)<=10:
        print("#{} {}".format(tc + 1, ' '.join(list(map(str, res[::-1])))))
    else:
        print("#{} {}".format(tc + 1, ' '.join(list(map(str, res[::-1][:10])))))