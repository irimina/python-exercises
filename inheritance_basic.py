'''
you can inherit genes from parents: nose, eyes - mom passed these traits to you automatically
also you can inherit a property ( i.e when a family member died you get part of her/his property - land, money, etc
getting something from someone else
'''


# create 2 classes and show how the class child gets properties from the the parent class

class Parent():

    def print_last_name(self):
        print('Roberts')

# in parenthesis you can put the class thet you want to inherit from
class Child(Parent):
    def print_first_name(self):
        print('James')


James = Child()

James.print_first_name()
James.print_last_name()

# the child can overide the function
'''

'''

