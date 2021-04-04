def add(a,tmpli):
    tmp.append(tmpli[a])
    for i in tmpli[a]:
        if i!=-1:
            add(i,tmpli)
    return tmp
t1=[[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# print(len(t1))
t2=[[-1, 1], [-1, -1]]
tmp1={i:[] for i in range(len(t1))}
for i in range(len(t1)):
    tmp1[i]+=t1[i]
print(tmp1)

tmp2 = {i:[] for i in range(len(t2))}
for i in range(len(t2)):
    tmp2[i]+=t2[i]
print(tmp2)
answer =0
for i in range(len(t1)):
    tmp=[]
    tmp_res = add(i,tmp1)
    if len(tmp_res)==len(tmp2):
        tmp2_res=add(0,tmp2)
        flag=0
        for j in range(len(tmp2)):
            if tmp2_res[j].count(-1)==0 and tmp_res[j].count(-1)==0:
                flag+=1
            elif tmp2_res[j].count(-1)==1 and tmp_res[j].count(-1)==1:
                if tmp2_res[j][0]==-1 and tmp_res[j][0]==-1:
                    flag+=1
                elif tmp2_res[j][1]==-1 and tmp2_res[j][1]==-1:
                    flag+=1
            elif tmp2_res[j].count(-1)==2 and tmp_res[j].count(-1)==2:
                flag+=1
        if flag==len(tmp2):
            answer+=1
print(answer)
# print(add(2))