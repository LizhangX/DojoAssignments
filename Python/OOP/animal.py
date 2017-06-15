
class Animal(object):
    def __init__(self, *args):
        # super(Animal, self).__init__(*args))
        self.name = args[0]
        self.health = args[1]

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "{}'s health is {}.".format(self.name.capitalize(), self.health)
        return self


animal1 = Animal("cat", 100)
animal1.walk().walk().walk().run().run().display_health()

class dog(Animal):
    def __init__(self, *args):
        super(dog, self).__init__(*args)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

dog1 = dog("doggie",100)
dog1.walk().walk().walk().run().run().pet().display_health()

class dragon(Animal):
    def __init__(self, *args):
        super(dragon, self).__init__(*args)
        self.health = 170
        
    def fly(self):
        self.health -= 10
        return self
    
    def display_health_dragon(self):
        self.display_health()
        print "I am a Dragon"
        return self

dragon1 = dragon("baby dragon",100)
dragon1.fly().display_health_dragon()