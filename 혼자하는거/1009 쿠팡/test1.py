temp_result = 0
temp_idx=0
for i in range(2,10):
    temp_trans=[]
    mother =10
    
    while mother>=i:
        res=mother%i
        temp_trans.insert(0,res)
        mother = mother // i
    temp_trans.insert(0,mother)
    # print(temp_trans,i)
    temp_mul=1
    for j in temp_trans:
        if j!=0:
            temp_mul*=j
    if temp_result <= temp_mul:
        temp_result=temp_mul
        temp_idx=i
print(temp_result,temp_idx)