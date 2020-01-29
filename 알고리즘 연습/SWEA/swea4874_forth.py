T=int(input())
for tc in range(1,T+1):
    a=list(input().split())
    flag=0
    stack=[]

    for i in range(len(a)-1):

        if a[i].isdigit():
            stack.append(a[i])

        else:
        
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if a[i]=="+":
                    
                    res = num1+num2
                    stack.append(str(res))

                elif a[i]=="-":
                    
                    res = num1-num2
                    stack.append(str(res))
                
                elif a[i]=="*":
                    
                    res = num1*num2
                    stack.append(str(res))
                    
                elif a[i]=="/":
                    
                    res = num1//num2
                    stack.append(str(res))
                
               
                
            except :
                flag = 189562165

    if flag == 0 and len(stack)==1:
        print("#{} {}".format(tc,stack[0]))

    if len(stack) > 1 or flag==189562165 :
        print("#{} {}".format(tc,"error"))
        
