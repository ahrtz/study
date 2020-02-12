T = int(input())

for tc in range(1,T+1):
    str1 = list(input()) #N, j
    str2 = list(input()) #M, i
    N = len(str1)
    M = len(str2)

    a_lst = []

    for i in range(M):
        for j in range(N):
            if str1[j]==str2[i]:
                a_lst.append(str2[i])
                str2.remove(str2[i])
                str2.insert(i, 0)

    a_lst_cnt = []

    for i in range(len(a_lst)):
        a_lst_cnt.append(a_lst.count(a_lst[i]))

    print('#{} {}'.format(tc, max(a_lst_cnt)))












    # a_lst = []
    #
    # i = 0
    # j = 0
    # while i<M and j<N:
    #     if str2[i] != str1[j]:
    #         i = i-j
    #         j = -1
    #     else:
    #         a_lst.append(str2[i])
    #
    #     i = i + 1
    #     j = j + 1
    #
    # a_cnt_lst = []
    #
    # for i in range(len(a_lst)):
    #     a_cnt_lst.append(a_lst.count(a_lst[i]))
    #
    # print(a_lst)
    # print(a_cnt_lst)
    #
    # print('#{} {}'.format(tc, max(a_cnt_lst)))


    # a_lst = []
    # dic = {}
    #
    # for i in range(M):
    #     for j in range(N):
    #         if str2[i] == str1[j]:
    #             a_lst.append(str2[i])
    #
    # a_lst_cnt = []
    #
    # for i in range(len(a_lst)):
    #     a_lst_cnt.append(a_lst.count(a_lst[i]))

    # maxV = 0
    # test = []
    # for i in range(len(a_lst_cnt)):
    #     if a_lst_cnt[i] > maxV:
    #         maxV = a_lst_cnt[i]
    #
    # x = 0
    # for i in range(len(a_lst_cnt)):
    #     if a_lst_cnt[i] == maxV:
    #         x = i

    # print(a_lst)
    # print(a_lst_cnt)
    # print('#{} {}'.format(tc, max(a_lst_cnt)))