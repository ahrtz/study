def solution(histogram):
    answer=0
    end_idx=len(histogram)-1
    # 가로길이 
    for start_idx in range(end_idx):
        for end_idx in range(len(histogram),start_idx,-1):
            garo = end_idx-start_idx-1
            sero = min(histogram[start_idx],histogram[end_idx])
            if answer<garo*sero:
                answer=garo*sero
    # start_idx=0

    return answer

histogram = [2, 2, 2, 3]
end_idx=len(histogram)-1
# 가로길이 
answer=0
for start_idx in range(end_idx):
    for end_idx in range(len(histogram)-1,start_idx,-1):
        garo = end_idx-start_idx-1
        sero = min(histogram[start_idx],histogram[end_idx])
        if answer<garo*sero:
            answer=garo*sero
print(answer)