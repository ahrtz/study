#tri = int(input())

#for i in tri:
floor = int(input())
room = int(input())
mem= []
cnt = 0    

for i in range(1,room+1):
    mem.append(i)

if floor ==1 :
    for i in range(room+1):
        cnt+=i
    print(cnt)
else:

/////////
T = int(input())

for n in range(T):

    k = int(input())

    n = int(input())

    people = [ i for i in range(1, n+1)]

    for nm in range(k):

        for j in range(1,n):

            people[j] += people[j-1]

    print(people[-1])