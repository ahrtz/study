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
    N,M,L  = map(int,input().split())
    numbers = list(map(int,input().split()))
    
    Head = None
    addtoFirst(numbers[0])
    
    for node in numbers[1:]:
        addtoLast(node)
    
    for _ in range(M):
         # 헤드 처음부터
        pre = Head
        cnt=0
        tmp = list(input().split())
        while pre.link != None: # 맨 끝까지 돌면서 찾기
            if tmp[0]=='I': # 넣기
                if int(tmp[1])==0:
                    addtoFirst(int(tmp[2]))
                    break
                elif cnt == int(tmp[1])-1:
                    add(pre,int(tmp[2]))
                    break
                else:
                    pre=pre.link
                    cnt+=1
            if tmp[0]=='D':
                if int(tmp[1])==0:
                    Head=Head.link
                    break
                elif cnt == int(tmp[1])-1:
                    delete(pre)
                    break
                else:
                    pre=pre.link
                    cnt+=1
            if tmp[0]=='C':
                # if int(tmp[1])==0:
                #     Head.item = int(tmp[2])
                #     break
                if cnt == int(tmp[1]):
                    pre.item = int(tmp[2])
                    break
                else:
                    pre=pre.link
                    cnt+=1
    # 이제 출력
    cnt =0
    pre=Head
    res='a'
    while pre.link!=None:
        if cnt == L:
            res = pre.item
            # print(pre.item)
            # pre=pre.link
            break
        else:
            cnt += 1
            # print(pre.item)
            pre=pre.link
    # print(pre.item)
    if res=='a':
        res=pre.item
    if cnt <L:
        res=-1
    print ("#{} {}".format(tc+1,res))
    