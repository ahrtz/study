words=["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries=["fro??", "????o", "fr???", "fro???", "pro?"]

answer=[]
for query in queries: 
    cnt=0
    
    for word in words:
        flag=123
        if len(word)!=len(query):
            continue
        elif query=='?'*len(query) and len(query)==len(word):
            cnt+=1
        elif query[0]=='?':
            qnum=query.count('?')
            if query[qnum:]==word[qnum:]:
                cnt+=1
        else:
            qnum=query.count('?')
            if query[:(len(query)-qnum)]==word[:(len(query)-qnum)]:
                cnt+=1
        
    answer.append(cnt)
print(answer)