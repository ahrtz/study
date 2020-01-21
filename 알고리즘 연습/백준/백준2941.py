word= input()

word=word.replace("c=","1")
word=word.replace("c-","2")
word=word.replace("dz=","3")
word=word.replace("d-","4")
word=word.replace("lj","5")
word=word.replace("nj","6")
word=word.replace("s=","7")
word=word.replace("z=","8")

word_li=[]
for i in word:
    word_li.append(i)

print(len(word_li))



