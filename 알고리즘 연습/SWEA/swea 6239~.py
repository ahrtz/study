# a= input()

# protocol_idx=a.find("://")
# others_idx=a.find("/",protocol_idx+3)

# print("protocol: {}".format(a[:protocol_idx]))
# print("host: {}".format(a[protocol_idx+3:others_idx]))
# print("others: {}".format(a[others_idx+1:]))

#############################################6678

# while True:
    
#     a=input()
#     print(">> {}".format(a.upper()))    
#     if a =="":
#         break
############################################6243

# a= list(map(str,input().split()))
# b=set(sorted(a))
# b=sorted(b)
# print(",".join(str(i)for i in b))
########################6248

a= input()
b=[]
for i in range(len(a)):
    if i %2 ==0:
        b.append(a[i])

print("".join(str(i) for i in b))

