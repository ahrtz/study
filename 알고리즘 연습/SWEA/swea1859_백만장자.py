def mil(prices):
    idx = prices.index(max(prices))
    




T=int(input())
for tc in range(1,T+1):
    days=int(input())
    prices = list(map(int,input().split()))
    if sorted(prices,reverse=True) == prices:
        print("#{} {}".format(tc,0))
    if sorted(prices)[-1] == prices[-1]:
        benefit = 0
        for i in range(len(prices)):
            benefit += (prices[-1]-prices[i])
        print("#{} {}".format(tc,benefit))
    