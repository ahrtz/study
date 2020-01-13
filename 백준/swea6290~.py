dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
 

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다','수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그','자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
result=[]
a_1=[]
a_2=[]
a_3=[]
a_4=[]
a_5=[]
a_6=[]
a_7=[]
a_8=[]
a_9=[]
a_10=[]
a_11=[]
a_12=[]
a_13=[]
a_14=[]
for i in inputWord:

    if ord(dicBase[0][0])<=ord(i[0])<=ord(dicBase[0][1]):
        a_1.append(i)
    elif ord(dicBase[1][0])<=ord(i[0])<=ord(dicBase[1][1]):           a_2.append(i)
    elif ord(dicBase[2][0])<=ord(i[0])<=ord(dicBase[2][1]):           a_3.append(i)
    elif ord(dicBase[3][0])<=ord(i[0])<=ord(dicBase[3][1]):           a_4.append(i)
    elif ord(dicBase[4][0])<=ord(i[0])<=ord(dicBase[4][1]):           a_5.append(i)
    elif ord(dicBase[5][0])<=ord(i[0])<=ord(dicBase[5][1]):           a_6.append(i)
    elif ord(dicBase[6][0])<=ord(i[0])<=ord(dicBase[6][1]):           a_7.append(i)
    elif ord(dicBase[7][0])<=ord(i[0])<=ord(dicBase[7][1]):           a_8.append(i)
    elif ord(dicBase[8][0])<=ord(i[0])<=ord(dicBase[8][1]):           a_9.append(i)
    elif ord(dicBase[9][0])<=ord(i[0])<=ord(dicBase[9][1]):           a_10.append(i)
    elif ord(dicBase[10][0])<=ord(i[0])<=ord(dicBase[10][1]):
        a_11.append(i)
    elif ord(dicBase[11][0])<=ord(i[0])<=ord(dicBase[11][1]):         a_12.append(i)
    elif ord(dicBase[12][0])<=ord(i[0])<=ord(dicBase[12][1]):         a_13.append(i)
    elif ord(dicBase[13][0])<=ord(i[0])<=ord(dicBase[13][1]):         a_14.append(i)
result.append(a_1)
result.append(a_2)
result.append(a_3)
result.append(a_4)
result.append(a_5)
result.append(a_6)
result.append(a_7)
result.append(a_8)
result.append(a_9)
result.append(a_10)
result.append(a_11)
result.append(a_12)
result.append(a_13)
result.append(a_14)
print(result)
        