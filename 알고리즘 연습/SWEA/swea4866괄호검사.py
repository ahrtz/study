
# sample = "print('{} {}'.format(1, 2))"


T= int(input())
for i in range(T):
    sample=input()
    a_1=sample.count("(")
    a=sample.index("(")
    b=sample.index(")")
    c=sample.index("{")
    d=sample.index("}")
    print(a_1)