def solution(numbers, hand):

    answer = ''
    left=[1,4,7]
    right = [3,6,9]
    mid=[2,5,8,0]
    leftidx=10
    rightidx=12
    for number in numbers:
        if number in left:
            answer+='L'
            leftidx = number
        if number in right:
            answer+='R'
            rightidx=number
        if number in mid:
            if number ==0:
                left_dis = abs(leftidx-11)%3+abs(leftidx-11)//3 
                right_dis = abs(rightidx-11)%3+abs(rightidx-11)//3 
            else:
                left_dis =abs(leftidx-number)%3+abs(leftidx-number)//3 
                right_dis = abs(rightidx-number)//3 + abs(rightidx-number) % 3 
            if left_dis==right_dis:
                if hand =="right":
                    answer+="R"
                    if number==0:
                        number=11
                    rightidx=number
                    
                else:
                    answer+="L"
                    if number==0:
                        number=11
                    leftidx = number
            elif left_dis<right_dis:
                if number==0:
                    number=11
                answer+='L'
                leftidx = number
            else:
                if number==0:
                    number=11
                answer+='R'
                rightidx=number
    return answer

solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")