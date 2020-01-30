a=int(input())

li=[]

for i in range(1,a+1):
    li.append(str(i))
final =[]
sam = ['3','6','9']
for i in li:
    for k in i:
        
        if k in sam:
            i=i.replace(k,"-")
    final.append(i)

for idx in range(len(final)):
    if final[idx].count('-')==1:
        final[idx]='-'
    elif final[idx].count('-')==2:
        final[idx]='--'
    elif final[idx].count('-')==3:
        final[idx]='---'





print(" ".join(final))
