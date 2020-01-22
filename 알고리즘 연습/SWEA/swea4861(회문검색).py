def isOk(n) : 
    s= str(n)
    return s==s[::-1]



a=int(input())
for i in range(a):
    length,str_length = map(int,input().split())
    table=[]
    result=[]
    for q in range(length):
        mstr=input()
        table.append(mstr)
    ## 세로 테이블 만들기 
    col_table=[]
    for cnt in range(len(table)):
        temp=[]
        for cnt_again in range(len(table)):
            temp.append(table[cnt_again][cnt])
        col_table.append("".join(temp))
    #가로검색
    for rows in table:
        temp2=[]
        for times in range(len(rows)-str_length+1):
            temp2.append(rows[0+times:str_length+times])
            for row in temp2:
                if isOk(row):
                    result.append(row)
    #세로검색
    for rows in col_table:
        temp2=[]
        for times in range(len(rows)-str_length+1):
            temp2.append(rows[0+times:str_length+times])
            for row in temp2:
                if isOk(row):
                    result.append(row)
    print("#{} {}".format(i+1,"".join(str(st) for st in result)))    

