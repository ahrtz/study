


T= int(input())
for i in range(T):
    sample=input()
    a=sample.count("(")
    b=sample.count(")")
    c=sample.count("{")
    d=sample.count("}")
    if a==b and c==d:
        print(1)
    else:
        print(0)