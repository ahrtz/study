# def find_route(r,c):
#     global result
#     if pan[r][c]==3:
#         result=1
#         return
#     else:
#         for i in range(len(d)):
#             dx,dy= d[i][0],d[i][1]
#             new_r = r+dx
#             new_c = c+dy

#             if 0<=new_r<16 and 0<=new_c<16 and (new_r,new_c) not in visited:
#                 if pan[new_r][new_c]==0:
#                     visited.append((new_r,new_c))
#                     find_route(new_r,new_c)
#                     visited.pop()

        


for _ in range(10):
    tc=int(input())
    pan=[]
    for _ in range(16):
        pan.append(list(map(int,input())))
    st=[]
    result=0
    for r in range(16):
        for c in range(16):
            if pan[r][c]==2:
                st.append((r,c))
                break
        if len(st)!=0:
            break
    d = ((1,0),(0,1),(-1,0),(0,-1))
    startx,starty=st[0][0],st[0][1]
    visited=[(startx,starty)]
    sp_point=[]
    cnt=0
    flag=0
    # find_route(startx,starty)
    while True:
        for i in range(len(d)):
            dx,dy= d[i][0],d[i][1]
            
            new_r = startx+dx
            new_c = starty+dy
            print(startx,starty)
            print(new_r,new_c)
            print(sp_point,cnt)
            if pan[new_r][new_c]==3:
                result=1
                break
            if 0<=new_r<16 and 0<=new_c<16 and (new_r,new_c) not in visited:
                                              
                if pan[new_r][new_c]==0:
                    sp_point.append((startx,starty))
                    visited.append((new_r,new_c))
                    sp_point.append((new_r,new_c))
                    startx=new_r
                    starty=new_c
                    cnt=0
            elif cnt==4:
                          
                tmp=sp_point.pop()
                startx = tmp[0]
                starty = tmp[1]
                cnt=0

            # if len(sp_point)==0:
            #     break
            elif pan[new_r][new_c]==1 or (new_r,new_c) in visited:
                cnt += 1
            # if cnt==4 and 

        if result==1 or (len(sp_point)==0 and cnt == 4):
            break
    print("#{} {}".format(tc,result))
