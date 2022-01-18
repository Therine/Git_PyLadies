#The Cat can meow with the meow method.
#The Cat has 9 lives when she's created (she can't have more than 9 and less than 0 lives).
#The Cat can say if she is alive (has more than 0 lives) with the alive method.
#The Cat can lose lives (method takeoff_life).
#The Cat can be fed with the eat method that takes exactly 1 argument - a specific food (string). If the food is fish, the Cat will gain one life (if she is not already dead or doesn't have maximum lives).

class Cat:
    def __init__(self, name):
        self.name = name
        self.lives = 9

    def meow(self):
        print("{}: Meow!".format(self.name))

    def alive(lives):
        print("{} has {} lives.".format(self.name, self.lives))

    def takeoff_life(lives):
        print("{} jumped out of a really high window.".format(self.name))
        self.lives = self.lives - 1
        if self.lives >=1:
            print("Oh, no! {} now has only {} lives!".format(self.name, self.lives))
        else:
            print("{} has died!".format(self.name))
    
        

pippen = Cat("Pippen")
print(pippen)