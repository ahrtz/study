class Rectangle:
    length = 4
    height = 5


    def area(self):
        return (self.length *self.height)

    def show(self):
        print("사각형의 면적: {}".format(Rectangle.area(self)))

Rectangle().show()