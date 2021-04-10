def timectosec(timedata):
    temp = timedata.split(":")
    hourtosec = int(temp[0])*60*60
    mintosec = int(temp[1])*60
    sec= int(temp[2])
    return hourtosec+mintosec+sec

def sectostr(timedata):
    hour = timedata//(60*60)
    if len(str(hour))==1:
        str_hour="0"+str(hour)
    else:
        str_hour=str(hour)
    minute = (timedata %3600)//60
    if len(str(minute))==1:
        str_minute="0"+str(minute)
    else:
        str_minute=str(minute)
    sec = (timedata %3600)%60
    if len(str(sec))==1:
        str_sec="0"+str(sec)
    else:
        str_sec=str(sec)
    return str_hour+":"+str_minute+":"+str_sec


def solution(play_time, adv_time, logs):
    
    playend = timectosec(play_time)
    adv = timectosec(adv_time)
    startlog=[]
    endlog=[]
    playtime_cnt=[0]*(playend+1)

    for i in logs:
        log_start,log_end = i.split("-")
        strt_time= (timectosec(log_start))
        end_time = (timectosec(log_end))
        playtime_cnt[strt_time]+=1
        playtime_cnt[end_time]-=1 # 여기가 인원 들락날락하는거 적어놓기
    ## 메모이제이션 무조건 
    for i in range(1,len(playtime_cnt)):
        playtime_cnt[i]=playtime_cnt[i]+playtime_cnt[i-1]  # 각 구간별 인원


    for i in range(1,len(playtime_cnt)):
        playtime_cnt[i]=playtime_cnt[i]+playtime_cnt[i-1]  # 누적인원 체크 

    print(playtime_cnt)
    most_view = 0                          
    max_time = 0                          
    for i in range(adv - 1, playend):
        if i >= adv:
            if most_view < playtime_cnt[i] - playtime_cnt[i - adv]:
                most_view = playtime_cnt[i] - playtime_cnt[i - adv]
                max_time = i - adv + 1
        else:
            if most_view < playtime_cnt[i]:
                most_view = playtime_cnt[i]
                max_time = i - adv + 1
    print(sectostr(max_time))
    return sectostr(max_time)

play_time = "02:03:55"

adv_time = "00:14:15"

logs = 	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

solution(play_time,adv_time,logs)