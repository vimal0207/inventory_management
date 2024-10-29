from datetime import datetime

from django.db import models

from base.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey("supplier.Supplier", on_delete=models.SET_NULL, null=True, blank=True)
    alert_threshold = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.name
    
    @property
    def is_low_stock(self):
        return self.quantity < self.alert_threshold
    
    @classmethod
    def get_low_stock_products(cls):
        return cls.objects.filter(quantity__lte=models.F('alert_threshold'))
    
    def add_stock(self, quantity, reason="Restock"):
        """Add stock to the product."""
        if self.quantity <= 0:
            return False, "Quantity must be greater than zero."
        self.quantity += quantity
        self.save()
        self.update_stock_change(quantity=quantity, reason=reason)
        return True, None

    def remove_stock(self, quantity, reason="Sale"):
        """Remove stock from the product."""
        if self.quantity < quantity:
            return False, "Cannot remove more stock than available."
        self.quantity -= quantity
        self.save()
        self.update_stock_change(quantity=-quantity, reason=reason)
        return True, None

    def update_stock_change(self, reason, quantity=None, date=None):
        data = {
            "product_id" : self.id,
            "quantity_changed" : quantity or self.quantity,
            "date_of_change" : date or datetime.now().date(),
            "reason" : reason
        }
        StockChange.objects.create(**data)
    
class StockChange(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_changed = models.IntegerField()
    date_of_change = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product.name}: {self.quantity_changed} - {self.reason} on {self.date_of_change}"