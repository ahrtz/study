n = 0
total = 0
user_input = int(input()) #input = 10  

if user_input>10000:
    print("만넘는거 안해줌")
else:
    while n <= user_input:
        total += n
        n += 1
    print(total)    #total = 55