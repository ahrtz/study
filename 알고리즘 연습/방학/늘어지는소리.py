T=int(input())
for tc in range(T):
    word = input()
    temp = [""]*(len(word)+1)
    H= int(input())
    h_list=list(map(int,input().split()))
    
    for idx in h_list:
        temp[idx]+="-"
    res=temp[0]
    for i in range(len(word)):
        res+=word[i]
        res+=temp[i+1]
    print("#{} {}".format(tc+1,res))