from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateField()
    
    @classmethod
    def _is_exist(self, name):
        return Customer.objects.filter(name=name).exist()
    
    @classmethod
    def _create_customer(self, msg):
        customer = Customer.objects.create(**msg)
        return customer