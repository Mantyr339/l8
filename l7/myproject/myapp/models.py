from django.db import models

class Client(models.Model):
    company_name = models.CharField(max_length=255)
    client_type = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

class Sale(models.Model):
    sale_date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    delivery_required = models.BooleanField()
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)