class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order and isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer and isinstance(new_customer, Customer):
            if new_customer not in self._customers:
                self._customers.append(new_customer)
        return self._customers
        # can also just use set() , instead of a nested if statement
        # return list(set(self._customers))
    
    def num_orders(self):
        return len([res.coffee for res in self._orders])
    
    def average_price(self):
        all_prices = [res.price for res in self._orders]
        return sum(all_prices) / len(all_prices)