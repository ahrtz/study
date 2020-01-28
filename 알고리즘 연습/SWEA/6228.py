class Shape():
    length = 0
    def area(self):
        return 0


class Square(Shape):
    length = 3


    def area(self):
        return self.length ** 2

    def show(self):
        print("정사각형의 면적: {}".format(Square.area(self)))

Square().show()