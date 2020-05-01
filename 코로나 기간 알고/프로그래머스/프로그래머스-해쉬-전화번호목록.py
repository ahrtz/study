
a=['12','123','1235','567','88']
def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x:len(x))
    while phone_book:
        tmp = (phone_book.pop(0))
        print(tmp)
        for i in range(len(phone_book)):
            if phone_book[i][0:len(tmp)]==tmp:
                answer = False
    return answer
print(solution(a))