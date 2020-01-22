a=int(input())
for i in range(a):
    my_str=input()
    mother_str=input()
    if my_str in mother_str:
        print("#{} {}".format(i+1,1))
    else:
        print("#{} {}".format(i+1,0))