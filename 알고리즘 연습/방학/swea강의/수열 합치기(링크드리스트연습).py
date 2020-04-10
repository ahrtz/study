def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)

def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoFirst(data):
    global Head
    Head = Node(data, Head)
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n

T = int(input())
for tc in range(T):
    
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))  
    # 노드로 삽입
    Head = None
    addtoFirst(numbers[0])
    # 나머지도 노드로 이어 붙이기
    for node in numbers[1:]:
        addtoLast(node)
    # 다음 수열 돌면서
    for _ in range(M - 1):
        temp_numbers = list(map(int, input().split()))
        pre = Head  # 수열의 맨 앞부터 다 돌면서 내가 필요한 지점 찾기
        while pre.link != None:
            if pre.link.item > temp_numbers[0]:  #넣을 인덱스 찾기
                break
            pre = pre.link
        # 넣기
        if pre == Head:  
            addtoFirst(temp_numbers[0])
            pre = Head  
            for item in temp_numbers[1:]:
                add(pre, item)
                pre = pre.link
        else:
            for item in temp_numbers:
                add(pre, item)
                pre = pre.link  
    # 일단 넣고 뒤집기
    pre = Head
    ans = [0] * N * M
    idx = 0
    while pre.link != None:
        ans[idx] = pre.item
        pre = pre.link
        idx += 1
    # 마지막꺼 넣기
    ans[idx] = pre.item  
    # 출력
    print("#{} {}".format(tc + 1, ' '.join(list(map(str, ans[::-1][:10])))))