giho =["+","-"]
giho1 = ["*","/"]
tmp=["("]

for tc in range(10):
    N=int(input())
    sik = list(input())
    num_list=[]
    giho_list=[]
    for digi in sik:
        if digi.isdigit():
            num_list.append(digi)
        if digi in tmp:
            giho_list.append(digi)
        if digi in giho:
            while True:
                if giho_list[-1] in giho1:
                    temp = giho_list.pop()
                    num_list.append(temp)
                    
                else:
                    giho_list.append(digi)
                    break
        if digi in giho1:
            while True:
                if giho_list[-1] in giho1:
                    temp = giho_list.pop()
                    num_list.append(temp)
                if giho_list[-1] in giho:
                    giho_list.append(digi)
                    break
                else:
                    giho_list.append(digi)
                    break
        if digi == ")":
            while True:
                temp = giho_list.pop()
                if temp == "(":
                    break
                if giho_list==[]:
                    break
                else:
                    num_list.append(temp)
    a=num_list

    flag=0
    stack=[]

    for i in range(len(a)):

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
    print(a)
    if flag == 0 :
        print("#{} {}".format(tc+1,stack[0]))

    if len(stack) > 1 or flag==189562165 :
        print("#{} {}".format(tc+1,"error"))
