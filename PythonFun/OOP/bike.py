
class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        # super(Bike, self).__init__(*args))
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayInfo(self):
        print "price: {}, max_speed: {}, total miles: {}".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):  
        print "Reversing"
        if self.miles < 0:
            self.miles = 0;
        return self


bike1 = Bike(200,"25mph")
# bike1.ride()     
# bike1.ride()     
# bike1.ride()
# bike1.reverse()
# bike1.displayInfo()
bike1.ride().ride().ride().reverse().displayInfo()
bike2 = Bike(300,"30mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

     