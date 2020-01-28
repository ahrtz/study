gumsa = ["{","}","[","]","(",")"]
T= int(input())
for i in range(T):
    result=[]
    sample = input()
    for alpha in sample:
        if alpha in gumsa:
            result.append(alpha)

    print(result)
    print(result.count("(",1))
    # print(result.index("("))
    