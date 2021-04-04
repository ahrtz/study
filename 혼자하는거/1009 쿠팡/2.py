def sol(n,customers):
    kiosk=[0]*n
    kiosk_cnt={i:0 for i in range(n)}

    for i in customers:
        
        day,hour,consume=i.split(" ")
        temp_time = int(day[0:2])*30*24*3600+int(day[3:5])*24*3600+int(hour[0:2])*3600+int(hour[3:5])+int(hour[6:])/60

        min_idx=kiosk.index(min(kiosk))
        kiosk[min_idx]=temp_time+int(consume)
        kiosk_cnt[min_idx]+=1
        print(kiosk)
        print(kiosk_cnt)
    print(max(kiosk_cnt.values()))
    pass
n=3
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

sol(n,customers)
a={0:1}
a[0]+=1
# print(a[0])

