def my_math():
    pi=3.14

    def circum(r):
        return  2*pi*r
    return circum
a=my_math()

print(a(1))
print(a(3))