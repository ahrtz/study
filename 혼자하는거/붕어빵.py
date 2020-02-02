t= int(input())
for tc in range(t):
    N_people,M_needtime,K_bread = map(int,input().split())
    people_li = list(map(int,input().split()))
    bbang=0
    



    # if M_needtime > min(N_peo_list):
    #     print("impossible")

    for t in range(1,max(people_li)+1):
        if t % M_needtime == 0:
            bbang += K_bread
            
        if t in people_li and bbang>0:
            for k in range(people_li.count(t)):
                people_li.pop(people_li.index(t))
                bbang -= 1
                # print(people_li)

    if len(people_li)==0:
        print ("#{} Possible".format(tc+1))
    else:
        print("#{} Impossible".format(tc+1))
                