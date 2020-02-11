def ok(n):
    if n==n[::-1]:
        return True
    else:
        return False
a=['C', 'B', 'B', 'C',"a"]
print(ok(a))