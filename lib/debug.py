#!/usr/bin/env python3
#import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    # print("HELLO! :) let's debug")
    gage = Customer("Gage")
    latte = Coffee("Latte")
    coldbrew = Coffee("Cold Brew")
    firstcoffee = Order(gage,latte,7)
    seccoffee = Order(gage,latte,8)
    Order(gage,coldbrew,4)
    print(latte.num_orders())
    print(latte.average_price())
    # print(latte.customers())
    # print(gage.coffees())
    # print(gage.orders())
    #ipdb.set_trace()
