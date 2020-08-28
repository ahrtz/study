#쉽게해야댐
def check(word):
    
    tmpword = list(word.strip())
    tmp=[]
    while tmpword:
        poping = tmpword.pop(0)
        if poping ==')' :
            if len(tmp)==0:
                return False
            elif tmp[-1]=='(':
                tmp.pop()
        else:
            tmp.append(poping)
    if len(tmp)==0:
        return True
    else:
        return False



p="()))((()"
def changeword(p):
    if len(p)==2 :
        # print('%$')
        return '()'
    elif check(p):
        return p
    else:
        return '('+changeword(p[1:-1])+')'
def solution(p):
    if p=='':
        return ""
    elif check(p):
        return p
    else:
        for i in range(2,len(p)+1,2):
            # print(i,'$')
            tmp=p[:i]
            # print(tmp)
            if tmp.count('(')==tmp.count(')'):
                u=p[:i]
                v=p[i:]
                if check(u)==False:
                    # print(1)
                    tmpalpha=changeword(u)
                    # print(tmpalpha,'^%$')
                elif check(u)==True:

                    tmpalpha=u
                if check(v)==False and len(v)>2:
                    tmpbeta=solution(v)
                elif check(v):
                    tmpbeta=v
                return tmpalpha+tmpbeta
                


a=solution('()(())()')
print(a)


