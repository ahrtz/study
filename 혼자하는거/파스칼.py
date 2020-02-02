a= int(input())
for tc in range(a):
    num = int(input())
    numli=[[1],[1,1]]
    while len(numli)<num :
        temp = [1]
        for i in range(len(numli[-1])-1):
            temp.append(numli[-1][i]+numli[-1][i+1])
        temp.append(1)
        numli.append(temp)
    print(f"#{tc+1}")
    if num == 1:
        print(" ".join(str(a)for a in numli[0]))
    else:
        for k in range(len(numli)):
            print(" ".join(str(a)for a in numli[k]))
    # print("#{} {}".format(tc+1,numli)