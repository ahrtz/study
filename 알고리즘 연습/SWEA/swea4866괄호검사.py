<<<<<<< HEAD

# sample = "print('{} {}'.format(1, 2))"


T= int(input())
for i in range(T):
    sample=input()
    a_1=sample.count("(")
    a=sample.index("(")
    b=sample.index(")")
    c=sample.index("{")
    d=sample.index("}")
    print(a_1)
=======
gumsa = ["{","}","[","]","(",")"]
T= int(input())
for i in range(T):
    result=[]
    sample = input()
    for alpha in sample:
        if alpha in gumsa:
            result.append(alpha)
    check=[]
    #검사하기
    for k in range(len(result)):
        if result[k] =="(" or result[k]=="{":
            check.append(result[k])
        elif result[k] ==")" or result[k]=="}":
            if len(check)==0:
                check=[1]
                break
            elif check[-1]=="(" and result[k]==")" or check[-1]=="{" and result[k]=="}":
                check.pop()
            else:
                check=[11]
    if len(check)==0:
        print("#{} {}".format(i+1,1))
    else:
        print("#{} {}".format(i+1,0))

# print('{} {}'.format(1, 2))
    print(result)
    # print(result.count("("))
    # print(result.index("(",result.index("(")+1))
    
>>>>>>> acaa034a763853331baf38487d611a0e4fa308b5
