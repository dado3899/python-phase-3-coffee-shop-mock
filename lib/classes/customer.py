from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    def set_name(self,input):
        if type(input) is str and len(input) > 0 and len(input) < 16:
                self._name = input
        else:
            raise Exception("Not valid name")
    name = property(get_name,set_name)

    def orders(self):
        from .order import Order
        orderlist = []
        for order in Order.all:
            if order.customer == self:
                orderlist.append(order)
        return orderlist

    def coffees(self):
        from .order import Order
        coffeeslist = []
        for order in Order.all:
            if order.customer == self:
                if order.coffee not in coffeeslist:
                    coffeeslist.append(order.coffee)
        return coffeeslist
    
    def create_order(self,coffee,price):
        from .order import Order
        from .coffee import Coffee
        if type(coffee) is Coffee and type(price) is int:
            Order(self,coffee,price)
        else:
            raise Exception("Not valid inputs")