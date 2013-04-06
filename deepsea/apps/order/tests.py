"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.test import TestCase
from deepsea.apps.order.models import Order
from deepsea.apps.customers.models import Customers

class BaseTest(TestCase):
    msg = {
        'send_time':datetime.datetime.now(),
        'from':"大海啊大海",
        'people_number':3,
    }
    def setUp(self):
        pass
        
class CreateOrderTest(BaseTest):
    """docstring for OrderTest"""
    
    def test_sholud_create_order(self):
        wait_number = Order.foo(self.msg)
        self.asserEqual(wait_number, 'A-1')
        
