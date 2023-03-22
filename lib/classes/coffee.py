from classes.order import Order

class Coffee:
    def __init__(self, name):
        if type(name) is str:
            self._name = name
        self.uniquecus = []
    def get_name(self):
        return self._name
    def set_name(self,input):
        raise Exception("Can't change name")
    name = property(get_name,set_name)

    def orders(self):
        from .order import Order
        orderlist = []
        for order in Order.all:
            if order.coffee == self:
                orderlist.append(order)
        return orderlist
    
    def customers(self):
        return self.uniquecus

    def num_orders(self):
        from .order import Order
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    def average_price(self):
        from .order import Order
        totalprice = 0
        count = 0
        for order in Order.all:
            if order.coffee == self:
                totalprice += order.price
                count += 1
        return totalprice/count