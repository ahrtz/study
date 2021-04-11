gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]


start = 0
end=0 
gems_set=set(gems)
strt_idx=int(1e10)
end_idx=0
while start<=end and end<len(gems)+1  :
    print(gems[start:end])
    if set(gems[start:end])==gems_set:
        strt_idx=start
        end_idx=end
        break
    else:
        end+=1

print(strt_idx,end_idx)
