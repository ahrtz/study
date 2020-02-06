# def check(a,b):
#     #a는 시작 나사의 인덱스 ,b는 나머지 리스트
#     #뒤로만 붙인다.
      
#     if len(list(b))==0:
#         return res
#     for i in range(len(b)):
#         if a[-1] == b[i][0]:
#            res.append(b)
#            a=b[i]
#            b.pop(i)
           
#            check(a,b) 
#            return res
            
#         else:
#             return res


t=int(input())
for i in range(t):
    n=int(input())
    nasa=[]
    tmp = list(map(int,input().split()))
    temp=[]
    for lala in range(len(tmp)):
        if tmp.count(tmp[lala])==1:
            temp.append(tmp[lala])
    # print(temp)
    start=[] # 시작과 끝점 봅기
    end=[]
    for nod in temp:
        if tmp.index(nod) % 2 == 0:
            start.append((tmp[tmp.index(nod)],tmp[tmp.index(nod)+1]))
        else:
            end.append((tmp[tmp.index(nod)-1],tmp[tmp.index(nod)]))
    # print(start,end)  
    for k in range(0,len(tmp),2):
        nasa.append((tmp[k],tmp[k+1]))
    # print(nasa)
    # 시작 나사 정해주고 
    # 그다음부터 함수
    nasa.remove(start[0])
    nasa.remove(end[0])
    result = [start[0]]
    #print(nasa)
    while True:
        for nasaa in range(len(nasa)):
            if result[-1][-1]==nasa[nasaa][0]:
                result.append(nasa[nasaa])

            if len(result) == len(nasa)+1:
                break
        if len(result) == len(nasa)+1:
            break
    # print(result)
    result.append(end[0])
    finalre=[]
    for ffinal in range(len(result)):
        finalre.append(result[ffinal][0])
        finalre.append(result[ffinal][1])
    print("#{} {}".format(i+1," ".join(repr(l) for l in finalre)))
    
