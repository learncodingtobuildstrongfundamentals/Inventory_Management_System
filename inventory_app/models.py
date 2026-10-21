from django.db import models

class Supplier(models.Model):
    name=models.CharField(max_length=25)
    contact_email=models.EmailField(max_length=25)
    phone=models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity=models.IntegerField()
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return self.name
