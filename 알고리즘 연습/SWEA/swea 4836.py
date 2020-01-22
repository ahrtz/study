a= int(input())
for i in range(a):
    num= int(input())
    panel_list=[]
    red=[]
    bl=[]
    dot_1=[[0 for col in range(10)] for row in range(10)]
    
    for k in range(num):
        panel_list.append(list(map(int,input().split())))
    for panel in panel_list:
        if panel[-1] == 1:
            red.append(panel)
        else:
            bl.append(panel)
    for red_dot in red:
        for x_ in range(red_dot[0],red_dot[2]+1):
            for y_ in range(red_dot[1],red_dot[3]+1):
                dot_1[x_][y_]=1
    for bl_dot in bl:
        for x_ in range(bl_dot[0],bl_dot[2]+1):
            for y_ in range(bl_dot[1],bl_dot[3]+1):
                if dot_1[x_][y_]!=None:
                    dot_1[x_][y_]+=2
                else:
                    dot_1[x_][y_]=2
    cnt= 0
    for aaa in range(10):
        cnt+= dot_1[aaa].count(3)
    print("#{} {}".format(i+1,cnt))

