def solution(record):
    answer = []
    records=[]
    nickname=dict()
    recordss = [i.split(' ') for i in record]
    print(recordss)
    for rec in record:
        tmp_record = list(rec.split())
        records.append(tmp_record)
    for record in records:
        if record[0]=="Enter" or record[0]=='Change':
            nickname[record[1]]=record[2]
    for record in records:
        if record[0]=='Enter':
            answer.append(nickname[record[1]]+"님이 들어왔습니다.")
        elif record[0]=='Leave':
            answer.append(nickname[record[1]]+"님이 나갔습니다.")
    
    return answer





