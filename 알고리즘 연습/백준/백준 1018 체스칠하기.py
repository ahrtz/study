import pprint
l,h= map(int,input().split())

chess_mom=[]
for j in range((l)):
    chess_mom.append(list(input()))

resu=[]
for i in range(l-7):
    for j in range(h-7): # 판 짤라내기
        cnt=0
        cnt1=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (i+j-k-l)%2==0: # 시작이 B이면 
                    if chess_mom[k][l]=="W":
                        cnt+=1
                else:
                    if chess_mom[k][l]=="B":
                        cnt+=1
        resu.append(cnt)




        for k in range(i,i+8):
            for l in range(j,j+8):        
                if (i+j-k-l)%2==0: # 시작이 B이면 
                    if chess_mom[k][l]=="B":
                        cnt1+=1
                else:
                    if chess_mom[k][l]=="W":
                        cnt1+=1                        
                
        resu.append(cnt1)
        

   
    
print(min(resu))