def solution(flowers):
    day=[0]*366
    for i in flowers:
        for days in range(i[0],i[1]):
            day[days]=1
        
    return day.count(1)

flowers = [[3, 4],[4, 5], [6, 7], [8, 10]]

day=[0]*365
for i in flowers:
    for days in range(i[0],i[1]):
        day[days]=1
print(day)
print(day.count(1))