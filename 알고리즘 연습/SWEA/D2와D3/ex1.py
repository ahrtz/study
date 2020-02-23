a=[(5,8,3),(4,2,3),(2,10,3),(2,2,6)]
a= sorted(a,key= lambda x:(x[2],x[0]))
print(a)
a.remove(a[-2])
print(a)
