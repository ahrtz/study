# def solution(N):

#     return




a= int(input())

b=[]

while True:
    tmp=a%3
    a=a//3
    if tmp ==0:
        b.insert(0,4)
    elif tmp ==1:
        b.insert(0,1)
    elif tmp ==2:
        b.insert(0,2)
    if a<3:
        break
b.insert(0,a)
print(tmp)
print(b)


# while a//4>=1:
#     tmp=str(a%4)
#     m=str(a//4)
#     a=a//4
#     if tmp=="1":
#         b.insert(0,tmp)
#     elif tmp == "2":
#         b.insert(0,tmp)
#     elif tmp == "0" :
#         b.insert(0,"4")
#     elif tmp == "3":
#         b.insert()
# if m == "1":
#     b.insert(0,"1")
# elif m=="2":
#     b.insert(0,"2")
# elif m=="0":
#     b.insert(0,"4")


res = "".join(repr(k) for k in b)    
print(res)

