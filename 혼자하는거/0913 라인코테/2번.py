def solution(ball, order):
    tmp_order=[]
    answer = []
    for i in order:
        # print(ball,"#",answer,i)
        if ball[0]==i or ball[-1]==i:
            ball.remove(i)
            answer.append(i)
            while True:
                checked = [0]*len(tmp_order)
                for j in range(len(tmp_order)):
                    if checked[j]==0:
                        if ball[0]==tmp_order[j] or ball[-1]==tmp_order[j]:
                            ball.remove(tmp_order[j])
                            answer.append(tmp_order[j])
                            tmp_order.remove(tmp_order[j])
                            checked = [0]*len(tmp_order)
                            break
                        else:
                            checked[j]=1
                if checked==[1]*len(tmp_order):
                    break
        else:
            tmp_order.append(i)
    
    
    return answer


ball=[1, 2, 3, 4, 5, 6]
order=	[6, 2, 5, 1, 4, 3]

print(solution(ball,order))