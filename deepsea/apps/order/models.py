from django.db import models
from deepsea.apps.order import TABLE
from deepsea.apps.customer.models import Customer as C

class Order(models.Model):

    customer = models.ForeignKey(C)
    send_date = models.DateField()
    wait_number = models.IntegerField()
    people_number = models.IntegerField()
    table_style = models.CharField(max_length=10)
    
    @classmethod
    def _get_wait_number(self, table_style):
        """获取最近的票号"""
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        today_orders = Order.objects.filter(send_date=now, table_style=table_style)
        #如果存在today_orders则返回number+1 若没有，则返回数字1
        latest_number = today_orders and today_orders.reverse()[0].number or 0
        new_number = latest_number + 1
        wait_number = "%(table_style)s-%(new_number)s" %locals()
        return wait_number
    
    @classmethod
    def foo(self, msg):
    """"处理微信收到的文本信息，返回订单号"""
        #是否存在该客户
        data = {}
        name = msg['from']
        customer = C._is_exist(name) and C._create_customer(**msg) or C.objects.get(name=name)
        #获取票号
        table_style = TABLE[msg['people_number']]
        msg['table_style'] = table_style
        data["wait_number"] = Order._get_wait_number(table_style)
        data["customer"] = customer
        msg.update(data)
        order = Order.objects.create(**msg)
        return order.wait_number
    
    