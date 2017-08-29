# the class is like a template where you specify how you want the character to act and behave
# it is more than a collection of objects and functions
# the character can an object of the class

class Enemy:
    life = 3
    '''
    self means use something from this own class
    i.e use the attack function in this class, or self life means use the variable life in this class, etc

    '''
    def attack(self):
        print('ouch')
        # subtract 1 from enemy's life
        # life= life -1 WRONG
        self.life-=1 # this accesses the variable inside the class

    def checkLife(self):
        if self.life<=0:
            print('I am dead')
        else:
            print(str(self.life), 'lives left')



# now when you attack you can't just say attack(), you need to create an object

# the object enemy 1 you set it equal to the class that you want to use stuff from
# enemy1 is an object from class Enemy so go to class Enemy and use the attack function
enemy1=  Enemy()
enemy2=Enemy()


enemy1.attack()
#enemy1.checkLife()

enemy1.attack()

print('How many lives does enemy 1 still have?')
enemy1.checkLife()

print('How many lives does enemy 2 still have?')
enemy2.checkLife()

# now we have enemy2; we have 2 objects, copies from this class and we store it in a variable called enemy2
# each object here has 3 lives each
# so when you attack enemy1, it doesn't affect enemy 2
# each object is independent of one another
