def solution(companies, applicants):
    answer = []
    each_com =[]
    each_app=[]
    for i in companies:
        each_com.append(list(i.split(' ')))
    for i in applicants:
        each_app.append(list(i.split(' ')))
    for i in range(len(each_app)):
        each_app[i][2]=int(each_app[i][2])
    rounds={each_com[i][0]:[] for i in range(len(each_com)) }
    # print(rounds)
    print(each_com,each_app)
    while each_app:
        for i in each_app:
            if rounds[i[1][0]].count(i[0])==0:
                rounds[i[1][0]].append(i[0])
                i[2]-=1
        for i in each_app:
            if i[2]==0:
                each_app.remove(i)

        for i in range(len(rounds)):
            if len(rounds[each_com[i][0]])> int(each_com[i][2]):
                tmp_list=[]
                for favor in each_com[i][1]:
                    if favor in rounds[each_com[i][0]]:
                        tmp_list.append(favor)
                    if len(tmp_list)==int(each_com[i][2]):
                        rounds[each_com[i][0]]=tmp_list
                        break
    print(rounds)
    return rounds


companies = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
answer = []
each_com =[]
each_app=[]
flag=1
for i in companies:
    each_com.append(list(i.split(' ')))
for i in applicants:
    each_app.append(list(i.split(' ')))
for i in range(len(each_app)):
    each_app[i][2]=int(each_app[i][2])
    each_app[i].append(0)
rounds={each_com[i][0]:[] for i in range(len(each_com)) }
# print(rounds)
print(each_com,each_app)
while each_app:
    for i in each_app:
        for j in rounds:
            if rounds[j].count(i[0])!=0:
                continue
            else:
                if rounds[i[1][i[3]]].count(i[0])==0:
                    rounds[i[1][i[3]]].append(i[0])
                    i[2]-=1
                    i[3]+=1
    for i in each_app:
        if i[2]==0:
            each_app.remove(i)
    
    for i in range(len(rounds)):
        if len(rounds[each_com[i][0]])> int(each_com[i][2]):
            tmp_list=[]
            for favor in each_com[i][1]:
                if favor in rounds[each_com[i][0]]:
                    tmp_list.append(favor)
                if len(tmp_list)==int(each_com[i][2]):
                    rounds[each_com[i][0]]=tmp_list
                    flag=23
                    break
        
    
print(rounds)

# solution(companies,applicants)