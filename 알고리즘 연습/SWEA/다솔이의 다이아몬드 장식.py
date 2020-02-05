t=int(input())

for tc in range(t):
    a=input()
    print(".{}".format('.#..'*len(a)))
    print(".{}".format("#.#."*len(a)))
    for k in range(len(a)):
        print(f"#.{a[k]}.", end="")
    print("#")
    print(".{}".format("#.#."*len(a)))
    print(".{}".format('.#..'*len(a)))


