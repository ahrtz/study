a=int(input())
start =1 
end = a**2
while (end-start)/2>0.000005:
    if ((start+end)/2)**2 < a < end:
        start = (start+end)/2
    elif start **2 < a < ((end+start)/2)**2:
        end = (start+end)/2
    print("#")
    print("!")
print(start,end)