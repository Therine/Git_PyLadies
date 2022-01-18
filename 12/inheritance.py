class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{}: I like {} very much!".format(self.name, food))


class Kittie(Animal):
    def meow(self):
        print("{}: Meow!".format(self.name))


class Doggie(Animal):
    def woof(self):
        print("{}: Woof!".format(self.name))


smokey = Kittie('Smokey')
doggo = Doggie('Doggo')
smokey.meow()
doggo.woof()
smokey.eat('mouse')
doggo.eat('bone')