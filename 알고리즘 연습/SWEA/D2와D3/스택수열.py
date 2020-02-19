import sys
def append(a,b):
    return a.append(b)

N=sys.stdin.readline() 
# N=int(input())
N=int(N)
stack=[]
num_list=set(range(1,N+1))
result=[]
flag=0
for i in range(N):
    # a=int(input())
    a=sys.stdin.readline()
    a=int(a)
    if stack==[]: # 초기단위
        for l in range(1,a+1):
            stack.append(l)
            append(result,"+")
            try:
                num_list.remove(l)
            except :
                pass
            
        stack.pop()
        append(result,"-")
           
    elif stack[-1]<a:
        for l in num_list:
            if l <= a :
                append(stack,l)
                append(result,"+")
        for num in stack:
            if num in num_list:
                num_list.remove(num)
        stack.pop()
        append(result,"-") 
    elif stack[-1] == a:
        stack.pop()
        append(result,"-")

    else:
        flag=1
        
if flag==0:
    for q in result:
        print(q)
elif flag==1:
    print("NO")
