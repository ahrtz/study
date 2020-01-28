class Circle:
    rad = 2





    def area(self):
        return (self.rad **2)* 3.14

    def show(self):
        print("원의 면적: {}".format(Circle.area(self)))

Circle().show()