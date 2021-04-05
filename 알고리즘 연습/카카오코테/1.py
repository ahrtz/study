def solution(new_id):
    answer = ''
    alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","-","_","."]
    temp_id_1 = new_id.lower()
    temp_id_2=""
    for i in temp_id_1:
        if i in alphabet_list:
            temp_id_2+=i
    temp_id_3 = ""
    cnt=0
    for i in temp_id_2:
        if i==".":
            cnt+=1
        else:
            if cnt>=1:
                temp_id_3+="."
                cnt=0
            
            temp_id_3+=i
    
    
        
    if temp_id_3 and temp_id_3[0]==".":
        temp_id_3=temp_id_3[1:]
    if temp_id_3 and temp_id_3[-1]==".":
        temp_id_3=temp_id_3[:-1]
    if temp_id_3=="":
        temp_id_3="a"
    if len(temp_id_3)>=16:
        temp_id_3=temp_id_3[:15]
        
    if temp_id_3[-1]==".":
        temp_id_3=temp_id_3[:-1]
    if len(temp_id_3)<=2:
        while len(temp_id_3)<3:
            temp_id_3+=temp_id_3[-1]
    # print(temp_id_3) 
    return temp_id_3

print(solution("...!@BaT#*..y.abcdefghijklm"))