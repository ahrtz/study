T=int(input())## 비트로 다시 해보겠습니다
dic_16={
    '0':'0000',    '1':'0001',    '2':'0010',    '3':'0011','4':'0100',
    '5':'0101',    '6':'0110',    '7':'0111',    '8':'1000','9':'1001',
    'A':'1010',    'B':'1011',    'C':'1100',    'D':'1101',
    'E':'1110',    'F':'1111'
}
for tc in range(T):
    num,l=input().split()
    num = int(num)
    l=list(l)
    # tmp=0 ## 이건 10진수로 바꿔서 2진수로 바꾸는거 
    # for i in range(num):
    #     tmp+= dic_16[l[i]]*16**(num-1-i)
    # answer=[]
    # while tmp!=1:
    #     a=tmp%2
    #     answer.insert(0,a)
    #     tmp=tmp//2
    # answer.insert(0,1)
    # print("#{} {}".format(tc+1,"".join(repr(k) for k in answer)))
    answer=[]
    for i in range(num):
        answer.append(dic_16[l[i]])
    print("#{} {}".format(tc+1,"".join(answer)))
