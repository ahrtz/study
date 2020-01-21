a= int(input())

for trial in range(a):
    num=int(input())
    temp=input()
    letter =[]
    for i in temp:
        letter.append(int(i))
    set_letter = set(letter)
    result = {}
    for k in set_letter:
        result[k] = letter.count(k)
    final = {}
    for key,val in result.items():
        if val == max(result.values()):
            final[key]=val
    if len(final)>=1:
        print("#{} {} {}".format(trial+1,max(final),final[max(final)]))
    