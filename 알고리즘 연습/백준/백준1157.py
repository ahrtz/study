word = input()
word=word.lower()

word_list = list(set(word))
word_cnt=[]
for spell in word_list:
    word_cnt.append(word.count(spell))

if (word_cnt.count(max(word_cnt)))>1:
    print("?")
else :
    print(word_list[word_cnt.index(1)].upper())