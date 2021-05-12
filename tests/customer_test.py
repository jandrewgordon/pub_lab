import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Craig", 69.00, 33)
        self.customer2 = Customer("Calum", 69.00, 13)
        self.customer3 = Customer("Andrew", 69.00, 26)

    def test_customer_has_money(self):
        self.assertEqual(69.00, self.customer.wallet)

    def test_buy_drink(self):
        drink = Drink('wine', 2.5, 1)
        pub = Pub('Pub', 100, [])
        pub.add_to_stock(drink, 10)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(1, self.customer.drunkeness)
        
    def test_buy_drink_fail(self):
        drink = Drink('wine', 2.5, 1)
        pub = Pub("Another pub", 100, [])
        pub.add_to_stock(drink, 10)
        self.customer2.buy_drink(drink, pub)
        self.assertEqual(0, self.customer2.drunkeness)
        
    def test_by_drink_drunk(self):
        drink = Drink("Moonshine", 5, 5)
        pub = Pub("Yet another pub", 100, [])
        pub.add_to_stock(drink, 5)
        self.customer3.buy_drink(drink, pub)
        self.customer3.buy_drink(drink, pub)
        self.assertEqual(5, self.customer3.drunkeness)
        
        
    def test_buy_food(self):
        food = Food("kebab", 2, 3)
        pub = Pub("Oh look another pub", 100, [food])
        self.customer3.buy_food(food, pub)
        self.assertEqual(-3, self.customer3.drunkeness)
        
        
    def test_adjust_stock(self):
        drink = Drink("wine", 3.5, 1)
        pub = Pub("Pub", 100, [])
        pub.add_to_stock(drink, 10)
        self.customer.buy_drink(drink, pub)
        self.assertEqual(9, pub.inventory[0]['stock_count'])
        
