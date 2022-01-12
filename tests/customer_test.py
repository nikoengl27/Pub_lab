import unittest
from unittest.case import TestCase

from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Captain Morgans", 5)
        self.customer = Customer("Jack Sparrow", 50)
    
    def test_customer_has_name(self):
        self.assertEqual("Jack Sparrow", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(50, self.customer.wallet)

    def test_can_reduce_wallet(self):
        self.customer.reduce_wallet(self.drink)    
        self.assertEqual(45, self.customer.wallet)

    

    