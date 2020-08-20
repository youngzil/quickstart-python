# !/usr/bin/python3

from collections import namedtuple

Customer = namedtuple('Customer', 'name is_88vip')
Product = namedtuple('Product', 'name price')


class Order:
    def __init__(self, customer, cart, promotion=None):
        """订单类

        Args:
            customer (Customer): 该订单的顾客
            cart (list): 购物车列表
            promotion (str, optional): 该订单享受的优惠，默认为 None
        """
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        """订单优惠前总额"""
        if not hasattr(self, '__total'):
            self.__total = sum(item.price for item in self.cart)
        return self.__total

    def due(self):
        """订单优惠后总额"""
        if self.promotion is None:
            discount = 0
        # 88vip打95折
        elif self.promotion == 'vip_discount':
            discount = self.total() * .05 if self.customer.is_88vip else 0
        # 每满300减40
        elif self.promotion == 'full_credit_discount':
            total = 0
            for item in self.cart:
                total += item.price
            discount = (total // 300) * 40
        # 满3减免单一件
        elif self.promotion == 'free_one_discount':
            if len(self.cart) >= 3:
                discount = min([item.price for item in self.cart])
            else:
                discount = 0
        return self.total() - discount

    def __repr__(self):
        fmt = '<订单 总价: {:.2f} 实付: {:.2f}>'
        return fmt.format(self.total(), self.due())


if __name__ == '__main__':
    joe = Customer('John Doe', True)
    cart_A = [Product('banana', 4),
              Product('apple', 10),
              Product('watermellon', 5)]

    print('策略一：为88vip顾客提供5%折扣')
    print(Order(joe, cart_A, "vip_discount"))

    cart_B = [Product('banana', 630),
              Product('apple', 410)]

    print('策略二：每满300减40活动')
    print(Order(joe, cart_B, "full_credit_discount"))

    cart_C = [Product('banana', 630),
              Product('apple', 410),
              Product('watermellon', 210)]

    print('策略三：满3件免单最便宜的一件')
    print(Order(joe, cart_C, "free_one_discount"))