numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
temp_small_num=min(numbers)
temp_large_num=max(numbers)

cnt_small = 0

temp=[]
for i in numbers:
    i=min(temp_large_num,temp_small_num)
    temp.append(i)
print(temp)

    
