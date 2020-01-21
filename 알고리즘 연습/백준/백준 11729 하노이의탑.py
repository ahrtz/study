
def hanoi(n,a,b,c):
    if n == 1 :
        print("{} {}".format(a,c))
        
    else:
        hanoi(n-1,a,c,b)
        print("{} {}".format(a,c))
        hanoi(n-1,b,a,c)
        


a= int(input())
print(2**(a)-1)
hanoi(a,1,2,3)
