def nqueen(sol,b):
    global count
    if len(sol)==b:
        count+=1
        return 0 
    candidate = list(range(b))
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        dis = len(sol)-i
        if sol[i]-dis in candidate:
            candidate.remove(sol[i]-dis)
        if sol[i]+dis in candidate:
            candidate.remove(sol[i]+dis)
    if candidate != []:
        for i in candidate:
            sol.append(i)
            nqueen(sol,b)
            sol.pop()
    else:
        return 0 



count = 0
num = int(input())
for i in range(num): # 첫 행의 경우의 수
    nqueen([i], num)
print(count)
