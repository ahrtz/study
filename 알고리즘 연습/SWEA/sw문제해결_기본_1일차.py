# for i in range(10):
#     apart_len=int(input())
#     apart = list(map(int,input().split()))
#     if apart[0] != 0 or apart[1] != 0 or apart[-1] != 0 or apart[-2] != 0:
#         break
#     cnt = 0
#     for k in range(2,apart_len-2):
#         a = apart[k]- apart[k-2]
#         b = apart[k]-apart[k-1]
#         c = apart[k]-apart[k+1]
#         d = apart[k]-apart[k+2]       
        
#         if a > 0 and b>0 and c>0 and d>0:
#             cnt += 1 * min(a,b,c,d)
        
#     print("#{} {}".format(i+1,cnt))
            
t= int(input())
for i in range(1,t+1):
    bat_num = int(input())
    carrots = list(map(int,input().split()))
    tot_carrots=sum(carrots)
    diff =[]
    
    A_carrot = 0
    for k in range(bat_num):
        A_carrot += carrots[k]
        B_carrot = tot_carrots-A_carrot
        diff.append(abs(A_carrot-B_carrot))
    idx=diff.index(min(diff))
    
    print("#{} {} {}".format(i,idx+1,min(diff)))    