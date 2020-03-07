def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)
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
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))  # 처음 거는 인풋 받아서 만들고
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
            if pre.link.item > temp_numbers[0]:  # 다음 거의 아이템이 나보다 크면
                break
            pre = pre.link
        # 아이템들을 거기에 넣어줌
        if pre == Head:  # 맨 앞에 들어가는 경우 Head를 업데이트
            addtoFirst(temp_numbers[0])
            pre = Head  # 이걸 안 써서 덮어씌워졌다. pre = pre.link말고 Head값을 가지고 돌도록 해야함
            for item in temp_numbers[1:]:
                add(pre, item)
                pre = pre.link
        else:
            for item in temp_numbers:
                add(pre, item)
                pre = pre.link  # 연결 잊지 말기
    # 최종 결과는 뒤집어서 출력
    pre = Head
    ans = [0] * N * M
    ind = 0
    while pre.link != None:
        ans[ind] = pre.item
        pre = pre.link
        ind += 1
    ans[ind] = pre.item  # while문 나오면서 마지막 거리를 안 넣어줬다....
    # 출력
    print("#{} {}".format(tc + 1, ' '.join(list(map(str, ans[::-1][:10])))))