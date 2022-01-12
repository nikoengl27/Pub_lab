import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jack Sparrow", 50)
        self.drink = Drink("Captain Morgans", 5)
        self.pub = Pub("The Prancing Pony", 100, [self.drink])

    def test_can_increase_till(self):
        self.pub.increase_till(self.drink)
        self.assertEqual(105, self.pub.till)


    # def test_can_sell_to_customer(self, customer):
    #     customer = Customer("Jack Sparrow", 50)
    #     self.customer.reduce_wallet(45, customer)
    #     self.pub.increase_till(105, self.pub.till)


    def test_can_sell_drink_to_customer(self):
        self.pub.can_sell_to_customer(self.customer, self.drink)
        self.assertEqual(105.00, self.pub.till)
        self.assertEqual(45, self.customer.wallet)