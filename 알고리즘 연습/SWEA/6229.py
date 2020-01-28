class Person:
    def getGender(self):
        return "Unknown"

class Male(Person):

    def getGender(self):
        return "Male"

    def show(self):
        return Male.getGender(self)
class Female(Person):

    def getGender(self):
        return "Female"

print(Male().show())
print(Female().getGender())