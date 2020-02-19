gumsa = ["{","}","[","]","(",")"]
flag=0
while True:
    tmp=""
    while True:
        sample = input()
        if len(sample)==1 and sample==".":
            flag=1
            break
        if sample[-1]==".":
            tmp += sample
            break
        else:
            tmp += sample

    if flag==1:
        break
    sample = tmp
    
    result=[]
    for alpha in sample:
        if alpha in gumsa:
            result.append(alpha)
    check=[]
    #검사하기

    for k in range(len(result)):
        if result[k] =="(" or result[k]=="[":
            check.append(result[k])
        elif result[k] ==")" or result[k]=="]":
            if len(check)==0:
                check=[1]
                break
            elif check[-1]=="(" and result[k]==")" or check[-1]=="[" and result[k]=="]":
                check.pop()
            else:
                check=[1]
    if len(check)==0:
        print("{}".format("yes"))
    else:
        print("{}".format("no"))
    