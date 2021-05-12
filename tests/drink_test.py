import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennants", 3.50, 1)

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drink.name)

    
        
