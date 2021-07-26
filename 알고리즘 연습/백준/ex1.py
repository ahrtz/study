answer=''

def jin2(num):
    global answer
    answer = str(num%2) + answer
    if num <2: 
        return num

    if num//2 == 1:
        answer = '1' + answer
    else: 
        answer = jin2(num//2)
    return  answer

print(jin2(0))
print(format(8,'b'))