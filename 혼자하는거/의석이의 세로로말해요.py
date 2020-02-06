T=int(input())
for tc in range(T):
    pan=[]
    for k in range(5):
        a=list(input())
        pan.append(a)
    # 가장 긴 문자열 길이 체크 
    tmp=[]
    for l in range(len(pan)):
        tmp.append(len(pan[l]))
    mmm=max(tmp)
    # print(max(tmp))
    for m in range(len(pan)):
        if len(pan[m])!=mmm:
            for cnt in range(mmm-len(pan[m])):
                pan[m].append("")
    # print(pan)
    res=[]
    print("#{}".format(tc+1),end=" ")
    for l in range(mmm):
        tmpp=[]
        for j in range(len(pan)):
            tmpp.append(pan[j][l])
        
        print("".join(str(k) for k in tmpp),end="")
    print()






# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx