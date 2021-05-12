class Pub:
    
    def __init__(self, name, till, inventory):
        self.name = name
        self.till = till
        self.inventory = inventory
        # self.drinks = drinks
        # self.food = food

    def add_funds(self, amount):
        self.till += amount
        
    def get_inv_object(self, search_string):
        for i in self.inventory:
            if search_string == i['item'].name:
                return i['item']

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def check_drunkeness(self, customer):
        if customer.drunkeness < 5:
            return True
        return False

    def decide_service(self, customer):
        if self.check_age(customer) and self.check_drunkeness(customer):
            return True
        
    def add_to_stock(self, item, stock_count):
        self.inventory.append({
                                "item" : item,
                                "stock_count" : stock_count
                                                            })
        
        
    def adjust_stock(self, item, amount):
        ## Will need loop if more than 1 item?
        for invent in self.inventory:
            if item == invent['item']:
                invent['stock_count'] += amount