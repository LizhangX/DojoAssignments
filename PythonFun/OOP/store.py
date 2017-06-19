
class store(object):
    def __init__(self, products,location,owner):
        # super(store, self).__init__(products,location,owner))
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def remove_product(self, productName):
        l = self.products.remove(productName)
        return self

    def inventory(self):
        print "All products: {}".format(self.products)
        return self

a = ["sdaf","asdf","gdfg","dfasdf"]

store1 = store(a, "123 road", "Mike")
store1.add_product("asdfaa").remove_product("sdaf").inventory()
    