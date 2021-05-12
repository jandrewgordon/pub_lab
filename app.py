from src.pub import *
from src.customer import *
from src.drink import *
from src.food import *

pub = Pub("Pub", 100, []) 

pub.add_to_stock(Food("margherita", 7, 4), 20)
pub.add_to_stock(Drink("beer", 3.5, 2), 100)
pub.add_to_stock(Food("chips", 4, 2), 200)
pub.add_to_stock(Drink("wine", 4, 2), 20)


calum = Customer('Calum', 20, 28)


print(calum.name, calum.wallet, calum.drunkeness)
calum.buy_drink(pub.get_inv_object("beer"), pub)
print(calum.name, calum.wallet, calum.drunkeness)

