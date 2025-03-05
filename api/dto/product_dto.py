class ProductDTO:
    def __init__(self, id, name, description, price, discount_rate, coupon_applicable, category_name):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.discount_rate = discount_rate
        self.coupon_applicable = coupon_applicable
        self.category_name = category_name
        self.discounted_price = self.get_discounted_price()

    def get_discounted_price(self):
        return self.price * (1 - self.discount_rate)
