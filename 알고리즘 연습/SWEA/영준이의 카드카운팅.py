T= int(input())
for tc in range(T):
    tmp = input()
    card_list=[]
    for c in range(0,len(tmp),3):
        card_list.append(tmp[c:c+3])
    for i in range(len(card_list)):
        if card_list.count(card_list[i])>1:
            print(f"#{tc+1} ERROR")
            break
    else:
        s=[]
        d=[]
        h=[]
        c=[]

        for card in card_list:
        
            if card[0]=="S":
                s.append(card)
            elif card[0]=="D":
                d.append(card)
            elif card[0]=="H":
                h.append(card)
            elif card[0]=="C":
                c.append(card)
        print(f"{tc+1} {13-len(s)} {13-len(d)} {13-len(h)} {13-len(c)}")