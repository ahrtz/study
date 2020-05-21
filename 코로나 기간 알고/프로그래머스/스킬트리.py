def solution(skill, skill_trees):
    answer =0
    for i in skill_trees:
        tmp=[]
        tmp1=[]
        flag=0
        for j in skill:
            if flag ==1:
                break
            if not tmp:
                print(i,j)
                if j in i:
                    tmp.append(i.index(j))
                else:
                    break
            else:
                for num in tmp:
                    if j in i:
                        if i.index(j)>num:
                            tmp.append(i.index(j))
                            tmp1.append(i)
                        elif i.index(j)<num:
                            flag=1
                            break
        if flag==0:
            print(i,'#')
            answer+=1
    return answer
skill = 'CBD'
ski = ["BACDE", "CBADF", "AECB", "BDA"]	
print(solution(skill,ski))
# print(skill.index('C'))