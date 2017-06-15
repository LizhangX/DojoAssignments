
class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status = "for sale"):
        # super(Product, self).__init__(*args))
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def Sell(self):
        self.status = "sold"
        return self
    
    def Add_tax(self, tax):
        self.price = self.price*(1+tax)
        return self
    
    def Return(self, reason):
        if reason == "defective":
            self.status = "defective"
        elif reason == "like_new":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price = self.price *0.8
        return self
        
    def Display_info(self):
        print "Price: {}".format(self.price)
        print "Item Name: {}".format(self.item_name)
        print "weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Cost: {}".format(self.cost)
        print "Status: {}".format(self.status)
        return self

product1 = Product(1000,"WoW","1kg","Blizzard",50)
product1.Sell().Add_tax(0.09).Return("opened").Display_info()