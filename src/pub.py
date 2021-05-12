class Pub:
    
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def add_funds(self, amount):
        self.till += amount

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
