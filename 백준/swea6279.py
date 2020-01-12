# a= int(input())
# result=[]
# for i in range(1,a+1):
#     if a % i == 0:
#         result.append(i)

# print(result)
# ---------------------------
# a = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
# result =[]
# for i in a:
#     if i %2 == 0:
#         result.append(i)

# print(result)
# -----------------------------
# pibo = [1,1]
# while len(pibo)<10:
#     new_pibo = pibo[-2]+pibo[-1]
#     pibo.append(new_pibo)
# print(pibo)
# 6288--------
# a=[]
# for i in range(1,21):
#     if i % 15 ==0:
#         pass
#     else:
#         a.append(i*i)
# print(a)
# 6289------------
a= input()
summ = 0
for i in range(len(a)):
    summ += int(a[i])
print(summ)