a= int(input())
print_num=0
if a >=60:
    for i in range(a-60, a+1): ## 이렇게 하면 60 미만의 수일때 에러가 나와버린다 
        list_num = list(map(int, str(i)))
        sum_num = i + sum(list_num)
        if(sum_num == a):
            print_num = i
            break
else: 
    for i in range(1, a+1): ## 이렇게 하면 60 미만의 수일때 에러가 나와버린다 
        list_num = list(map(int, str(i)))
        sum_num = i + sum(list_num)
        if(sum_num == a):
            print_num = i
            break

print(print_num)
############################################
# 런타임 에러가 왜 아래껀 안나고 위에건 나지
# N = int(input())
# print_num = 0
# for i in range(1, N+1):
#     div_num = list(map(int, str(i)))
#     sum_num = i + sum(div_num)
#     if(sum_num == N):
#         print_num = i
#         break
# print(print_num)