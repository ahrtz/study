a=int(input())

for i in range(a):
    A_wage,B_basic,B_limit_amount,B_wage,amount = map(int,input().split())

    # A 회사 
    A_tot = A_wage * amount
    # b 회사
    if amount > B_limit_amount:
        B_tot = B_basic + B_wage*(amount-B_limit_amount) 
    else:
        B_tot = B_basic

    if A_tot>=B_tot:
        result = B_tot
    else:
        result = A_tot
    print("#{} {}".format(i+1,result))