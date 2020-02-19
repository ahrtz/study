a=[(5,8,3),(4,2,3),(2,10,3),(2,2,6)]
a= sorted(a,key= lambda x:(x[2],x[0]))
a.remove(a[-2])
print(a)
b={1,2,3,4,5,6}
print(b)
b.remove(5)
print(b)