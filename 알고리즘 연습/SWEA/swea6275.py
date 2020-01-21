sentence ="Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
sentence =list(sentence)
alpha = ["a","e","i","o","u"]
for k in alpha:
    for i in range(sentence.count(k)):
        sentence.remove(k)


print("".join(str(item) for item in sentence))
