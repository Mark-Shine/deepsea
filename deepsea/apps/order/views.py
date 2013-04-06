#encoding=utf-8
from deepsea.apps.order.models import Order
from deepsea.apps.order import TABLE
from deepsea.apps.customer.models import Customer as C

def foo(msg):
    """"处理微信收到的文本信息，返回订单号"""
    #是否存在该客户
    data = {}
    name = msg['from']
    customer = C._is_exist(name) and C._create_customer(**msg) or C.objects.get(name=name)
    #获取票号
    table_style = TABLE[msg['people_number']]
    data["wait_number"] = Order._get_wait_number(table_style)
    data["customer"] = customer
    msg.update(data)
    order = Order.objects.create(**msg)
    return order.wait_number