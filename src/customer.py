class Customer:
    
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0

    def buy_drink(self, drink, pub):
        if pub.decide_service(self):
            self.wallet -= drink.price
            self.drunkeness += drink.alcohol_level
            
    def buy_food(self, food, pub):
        self.wallet -= food.price
        self.drunkeness -= food.rejuvination_level

