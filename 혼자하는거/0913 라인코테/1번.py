def solution(boxes):
    items=[]
    box_num1=len(boxes)
    box_num2=len(boxes)
    for i in boxes:
        items.append(i[0])
        items.append(i[1])

    for i in range(1,box_num1+1):
        if items.count(i)==2:
            box_num2-=1


    print(items)
    return box_num2
boxes=[[1, 1], [1, 1], [5, 6]]
print(solution(boxes))