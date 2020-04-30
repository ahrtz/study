def solution(answers):
    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5] * 1250
    c=[3,3,1,1,2,2,4,4,5,5] * 1000
    cnta=0
    cntb=0
    cntc=0
    for i in range(len(answers)):
        if a[i]==answers[i]:
            cnta+=1
        if b[i]==answers[i]:
            cntb+=1
        if c[i]==answers[i]:
            cntc+=1
    answer_list=[(1,cnta),(2,cntb),(3,cntc)]
    answer=[]
    for i in range(3):
        if answer_list[i][1]==max(cnta,cntb,cntc):
            answer.append(answer_list[i][0])
    return answer

