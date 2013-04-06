#encoding=utf-8
from order.models import Order
from customer.models import Customer as C

def function(msg):
    """"处理微信收到的文本信息，返回订单号"""
    #是否存在该客户
    data = {}
    name = msg['from']
    customer = C._is_exist(name) and C._create_customer(msg) or C.objects.get(name=name)
    #获取票号
    data["number"] = Order._get_number()
    data["customer"] = customer
    msg.update(data)
    order = Order.objects.create(**msg)
    return order.number