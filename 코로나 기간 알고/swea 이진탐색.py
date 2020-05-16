T=int(input())

def search(num_list,l,r,find_num,dir):
    global cnt
    m=(l+r)//2
    # print(m,'$$$$',num_list,find_num)
    if num_list[m]==find_num:
        cnt+=1
        # print(cnt,find_num,'&*^%$$@#!')
    else:
        if dir!='l' and num_list[m] > find_num:#왼쪽가기
            r=m-1
            search(num_list,l,r,find_num,'l')
        elif dir!='r' and num_list[m] < find_num:
            l=m+1
            search(num_list,l,r,find_num,'r')
    


for tc in range(T):
    a,b = map(int,input().split())
    
    a_list=list(map(int,input().split()))
    b_list=list(map(int,input().split()))
    a_list.sort()
    b_list.sort()
    cnt=0
    for num in b_list:
        if num in a_list:
            l=0 
            r=a-1
            search(a_list,l,r,num,0)
            m=(l+r)//2
            dir=[]
            
            while a_list:
                if a_list[m]==num:
                    # print(num)
                    cnt+=1
                    break
                elif a_list[m]>num: # 왼쪽갈거
                    r=m-1
                    m=(l+r)//2
                    dir.append('l')
                else:#오른쪽
                    l=m+1
                    m=(l+r)//2
                    dir.append('r')
                if len(dir)>1:
                    if dir[-1]==dir[-2]:
                        break
    
    
    print(f"#{tc+1} {cnt}")