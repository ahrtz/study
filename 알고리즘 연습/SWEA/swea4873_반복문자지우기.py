t= int(input())
for i in range(t):
    temp = list(input())
    temp_str=[]
    for k in range(len(temp)):
        if not temp_str or temp_str[-1] != temp[k]:# 리스트에 없거나 리스트에 있는거랑 다르면 리스트에 추가
            temp_str.append(temp[k])
            
        elif temp_str and temp_str[-1] == temp[k]:
            temp_str.pop()
            # 리스트에 있고 마지막거랑 같으면 저기서 빼라
    print("#{} {}".format(i+1,len(temp_str)))
    
            
    