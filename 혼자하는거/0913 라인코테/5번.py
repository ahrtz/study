def solution(cards):
    player=[]
    dealer=[]
    apoint=0
    for _ in range(2):
        a=cards.pop(0)
        if a>10:
            a=10
        player.append(a)
        b=cards.pop(0)
        if b>10:
            b=10
        dealer.append(b)
    showing=dealer[-1]
    while cards:
        
        if player==[]:
            for _ in range(2):
                a=cards.pop(0)
                if a>10:
                    a=10
                player.append(a)
                b=cards.pop(0)
                if b>10:
                    b=10
                dealer.append(b)
            showing=dealer[-1]


        if sumcard(player)==21:
            apoint+=3
            player=[]
            dealer=[]
        elif sumcard(dealer)==21:
            apoint-=2
            player=[]
            dealer=[]
        elif showing==1 or showing>=7:
            if sumcard(player)<17:
                player.append(cards.pop(0))
                if sumcard(player)>21:
                    apoint-=2
                    player=[]
                    dealer=[]
                if sumcard(player)==21:
                    if sumcard(dealer)!=21:
                        apoint+=3
                        player=[]
                        dealer=[]
                    else:
                        player=[]
                        dealer=[]
            else:
                if sumcard(dealer)<17:
                    dealer.append(cards.pop(0))
                    if sumcard(dealer)==21:
                        apoint-=2
                        player=[]
                        dealer=[]
                    if sumcard(dealer)>21:
                        apoint+=2
                        player=[]
                        dealer=[]
                    elif sumcard(dealer)>17 :
                        if sumcard(dealer)>sumcard(player):
                            apoint-=2
                            player=[]
                            dealer=[]
                        else:
                            apoint+=2
                            player=[]
                            dealer=[]
                elif 17<sumcard(dealer)<21:
                    if sumcard(dealer)>sumcard(player):
                        apoint-=2
                        player=[]
                        dealer=[]
                    else:
                        apoint+=2
                        player=[]
                        dealer=[]
        elif 3<showing<7:
            if sumcard(dealer)<17:
                dealer.append(cards.pop(0))
                if sumcard(dealer)>21:
                    apoint+=2
                    player=[]
                    dealer=[]
                if sumcard(dealer)==21:
                    apoint-=2
                    player=[]
                    dealer=[]
                elif sumcard(dealer)>17 :
                    if sumcard(dealer)>sumcard(player):
                        apoint-=2
                        player=[]
                        dealer=[]
                    else:
                        apoint+=2
                        player=[]
                        dealer=[]
            elif 17<sumcard(dealer)<21:
                if sumcard(dealer)>sumcard(player):
                    apoint-=2
                    player=[]
                    dealer=[]
                else:
                    apoint+=2
                    player=[]
                    dealer=[]
        elif 1<showing<4:
            if sumcard(player)<12:
                player.append(cards.pop(0))
                if sumcard(player)==21:
                    apoint+=3
                    player=[]
                    dealer=[]
                if sumcard(player)==21:
                    if sumcard(dealer)!=21:
                        apoint+=3
                        player=[]
                        dealer=[]
                    else:
                        player=[]
                        dealer=[]
            else:
                # print(dealer,'$')
                if sumcard(dealer)<17:
                    dealer.append(cards.pop(0))
                    if sumcard(dealer)>21:
                        apoint+=2
                        player=[]
                        dealer=[]
                    elif sumcard(dealer)==21:
                        apoint-=2
                        player=[]
                        dealer=[]
                    elif sumcard(dealer)>17 :
                        if sumcard(dealer)>sumcard(player):
                            apoint-=2
                            player=[]
                            dealer=[]
                        else:
                            apoint+=2
                            player=[]
                            dealer=[]

                elif 17<sumcard(dealer)<21:
                    if sumcard(dealer)>sumcard(player):
                        apoint-=2
                        player=[]
                        dealer=[]
                    else:
                        apoint+=2
                        player=[]
                        dealer=[]


    # print(apoint)
    # while cards:
    return apoint
def sumcard(card):
    if card.count(1)>0:
        for i in range(len(card)):
            tmpsum=sum(card)
            if card[i]==1:
                card[i]=11
                dealersum= sum(card)
                if dealersum<=21:
                    tmpsum=dealersum
                else:
                    break
        return tmpsum
    else:
        return sum(card)


cards= [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
solution(cards)



# def playersum(card):
#     tmpsum=0
#     if card.count(1)>0:
#         return
#     else:
#         return sum(card)