from django.db import models
from customer.model import Customer

class Order(models.Model):

    customer = models.ForeignKey(Customer)
    send_date = models.DateField()
    number = models.CharField(max_lenth=3)
    
    def _get_number(self, ):
        """获取最近的票号"""
        import datetime
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        today_orders = Order.objects.filter(send_date=now)
        #如果存在today_orders则返回number 若没有，则返回数字1
        latest_number = today_orders and today_orders.reverse()[0].number or 1
        return latest_number
    
    