def solution(tickets):
    start_idx=[]
    # tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    for sp in tickets:
        if sp[0]=='ICN':
            start_idx.append(sp)

    