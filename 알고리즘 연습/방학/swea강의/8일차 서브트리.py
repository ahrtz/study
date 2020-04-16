def counting(start):
    # 근데 이건 두개 일때만 되는건데.. 이진트리라서 두개다
    global cnt
    if start:
        counting(array[start][0])
        counting(array[start][1])
        cnt += 1


T = int(input())
for tc in range(T):

    # 간선의 개수 E, 루트 N
    E, N = list(map(int, input().split()))

    # 부모와 자식 노드 쌍 (노드 번호는 E+1까지 존재)
    array = [[0 for _ in range(2)] for __ in range(E+2)]
    lines = list(map(int, input().split()))
    for idx in range(0, len(lines), 2):
        if array[lines[idx]][0]:
            array[lines[idx]][1] = lines[idx+1]
        else:
            array[lines[idx]][0] = lines[idx+1]

    
    cnt = 0
    counting(N)
    print("#{} {}".format(tc+1, cnt))