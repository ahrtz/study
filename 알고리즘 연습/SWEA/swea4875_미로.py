T= int(input())
for tc in range(1,T+1):
    size = int(input())
    miro = [[0]*size for _ in range(size)]
    sec = [] # 2의 위치 인덱스 저장해놓기
    visit=[] # 갔던 곳 위치 인덱스 저장하기
    for k in range(size):    # 미로 형성하기
        locate = input()
        for l in range(len(locate)):
            miro[k][l]=int(locate[l])
            if locate[l]=="2":
                sec.append((k,l))
    start_x=sec[0][0]
    start_y=sec[0][1]
    print(miro)
    while True:
        #먼저 시작점의 사방을 검색
        try:
            #도착지부터
            if miro[start_x][start_y-1]==3 or miro[start_x][start_y+1]==3 or miro[start_x-1][start_y]==3 or miro[start_x+1][start_y]==3:
                print(1)
                break
            
            print(1)
            
            if miro[start_x][start_y-1]==0 and (start_x,start_y-1) not in visit: # 좌측검색
                print("#")
                start_y -= 1
                visit.append((start_x,start_y))
            if miro[start_x][start_y+1]==0 and (start_x,start_y+1) not in visit: # 우측검색
                print("#1")
                start_y += 1
                visit.append((start_x,start_y))
            if miro[start_x-1][start_y]==0 and (start_x-1,start_y) not in visit: # 상측검색
                start_x -= 1
                print("#2")
                visit.append((start_x,start_y))
            if miro[start_x][start_y+1]==0 and (start_x,start_y+1) not in visit: # 하측검색
                print("#3")
                start_y += 1
                visit.append((start_x,start_y))
        except:
            pass


