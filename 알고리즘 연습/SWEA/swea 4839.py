
def search(start_page,end_page,search_page,initial_cnt):
    cnt=initial_cnt
    c=int((start_page+end_page)/2)
    if start_page > end_page:
        return None




    elif c == search_page:
        cnt+=1
        # print('#', cnt)
        return cnt
    elif c > search_page:
        cnt+=1
        end_page=c
        # print('$', cnt)
    elif c < search_page:
        cnt+=1
        # search(c,end_page,search_page,cnt)
        start_page=c
        
    
    return search(start_page,end_page,search_page,cnt)
    



# tmp = search(1,400,50,0)
# print(tmp, type(tmp))




Test_case= int(input())
for i in range(Test_case):
    P,Pa,Pb = map(int,input().split())
    if Pa==P:
        cnta=0
        cntb= search(1,P,Pb,0)
    elif Pb==P:
        cnta= search(1,P,Pa,0)
        cntb=0
    elif Pa==1:
        cnta=0
        cntb= search(1,P,Pb,0)
    elif Pb==1:
        cnta= search(1,P,Pa,0)
        cntb = 0
    else:
        cnta= search(1,P,Pa,0)
        cntb= search(1,P,Pb,0)
    if cnta > cntb:
        print("#{} B".format(i+1))
    if cnta < cntb:
        print("#{} A".format(i+1))
    elif cnta == cntb:
        print("#{} 0".format(i+1))
