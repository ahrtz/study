def solution(blocks):
    prev_block = [blocks[0][1]]
    results=[blocks[0][1]]

    for i in range(1,len(blocks)):
        given_idx,given_number = blocks[i]
        cur_blocks = [given_number]

        for idx in range(given_idx-1,-1,-1):
            cur_blocks.insert(0,prev_block[idx]-cur_blocks[0])
        for idx in range(given_idx+1,i+1):
            cur_blocks.append(prev_block[idx-1]-cur_blocks[-1])
        
        results += cur_blocks
        prev_block = cur_blocks
    
    answer = results
    print(answer)
    return answer


solution([[0,50],[0,22],[2,10],[1,4],[4,-13]])