def check(p):
    tmpa=0
    tmpb=0
    for i in p :
        if i =='(':
            tmpa+=1
        else:
            tmpb+=1
    if tmpa!=tmpb:
        return False
    else:
        return True





def divideword(p):
    if p=='':
        return ""
    
    opnebra = 0
    closebra = 0
    endbra=""
    for i in range(len(p)):
        if p[i]=='(':
            opnebra+=1
        else:
            closebra+=1
        endbra=p[i]
        if opnebra==closebra: # 앞에꺼가 닫혓으면
            if endbra==')':
                return p[:i+1] + divideword(p[i+1:])
            else:
                print('$')
                return changeword(p[:i+1],divideword(p[i+1:]))

def changeword(u,v):
    empty='('
    empty += v + ')'
    for i in range(1,len(u)-1):
        if u[i]=='(':
            empty += ')'
        else:
            empty += '('
    return empty

def solution(p):
    if check(p):
        return p
    
    return divideword(p)
