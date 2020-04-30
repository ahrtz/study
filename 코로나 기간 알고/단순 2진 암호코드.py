T= int(input())
pwd_dic={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}
for tc in range(T):
    sero,garo = map(int,input().split())
    mapp=[]
    
    for i in range(sero):
        a=list(input())
        mapp.append(a)
        if '1' in a:
            tmp=a
    for k in range(len(tmp)-1,-1,-1):
        if tmp[k] =='1':
            # print(k)
            pwd=tmp[k-55:k+1]
            break
    
    pwd_list=[]
    for i in range(8):
        pwd_list.append("".join(pwd[0+7*i:7+7*i]))
    final_list=[0]*8
    for i in range(len(pwd_list)):
        final_list[i]=pwd_dic[pwd_list[i]]
    # 1242번
    veri = (final_list[0]+final_list[2]+final_list[4]+final_list[6])*3+final_list[1]+final_list[3]+final_list[5]+final_list[7]

    
    if veri%10==0:
        print("#{} {}".format(tc+1,sum(final_list)))
    else:
        print("#{} {}".format(tc+1,0))
