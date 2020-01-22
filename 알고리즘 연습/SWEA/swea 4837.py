from itertools import combinations

a= int(input())
A=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(a):
    sub_sum=[]
    len_num,sum_ex=map(int,input().split())
    sub=list(combinations(A,len_num))
    for sub_item in sub:
        sub_sum.append(sum(sub_item))    
    print("#{} {}".format(i+1,sub_sum.count(sum_ex)))


# for i in range(a):
#     sub=[]
#     len_num,sum_ex=map(int,input().split())
#     # for k in range(len(A)-2):
#     #     for p in range(k+1,len(A)-1):
#     #         for l in range(p+1,len(A)):
#     #             sub.append([k+1,p+1,l+1])
#     for subnum in range(len_num):

#     print(sub)
