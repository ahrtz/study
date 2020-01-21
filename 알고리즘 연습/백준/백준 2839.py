kg = int(input())

box = 0 

while True:
    if kg % 5 ==0:
        box = box+(kg //5)
        print(box)
        break
    kg -= 3
    box += 1
    if kg<0:
        print(-1)
        break
    








