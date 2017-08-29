# class vs instance of a class ( or class variable)

class Girl:

    # this common to all objects in the class, class variable
    gender = 'female'

    # this is unique to the object or that specific instance of the class; this is the instance variable
    def __init__(self, name):
        self.name = name

first_girl= Girl('Rachel')
another_girl = Girl('Sandy')

print(first_girl.gender)
print(another_girl.gender)

print(first_girl.name)
print(another_girl.name)
