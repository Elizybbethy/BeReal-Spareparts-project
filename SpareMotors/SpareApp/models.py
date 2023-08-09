from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category_name = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False
    )
    part_name = models.CharField(max_length=50, null=True, blank=False)
    arrival_date = models.DateField(default=timezone.now)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    unit_price = models.IntegerField(default=0, null=True, blank=False)
    country_of_origin = models.CharField(max_length=50, null=True, blank=False)
    branch_name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.part_name


class Sale(models.Model):
    part = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(default=0,null=False,blank=False)
    amount_received = models.IntegerField(default=0, null=False, blank=False)
    issued_to = models.CharField(max_length=100, null=True, blank=False)
    phone = models.CharField(max_length=30, null=True, blank=False)
    branch = models.CharField(max_length=50, null=True, blank=False)

    def get_total(self):
        total = self.quantity * self.part.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total - self.amount_received
        return abs(int(change))
    
    def __str__(self):
        return self.part.part_name
