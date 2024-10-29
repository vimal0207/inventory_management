from django.contrib import admin
from django.db import models
from .models import Product, Category, StockChange

admin.site.register(Category)
admin.site.register(StockChange)

class LowStockFilter(admin.SimpleListFilter):
    title = 'Low Stock'
    parameter_name = 'low_stock'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(quantity__lt=models.F('alert_threshold'))
        elif self.value() == 'No':
            return queryset.filter(quantity__gte=models.F('alert_threshold'))
        return queryset

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'quantity', 'price', 'category', 'supplier', 'display_is_low_stock')
    list_filter = ('category', 'supplier', LowStockFilter)
    search_fields = ('name', 'sku')
    
    def display_is_low_stock(self, obj):
        return obj.is_low_stock
    display_is_low_stock.short_description = 'Low Stock'
    display_is_low_stock.boolean = True

    def changelist_view(self, request, extra_context=None):
        low_stock_products = Product.get_low_stock_products()
        extra_context = extra_context or {}
        extra_context['low_stock_products'] = low_stock_products
        return super().changelist_view(request, extra_context=extra_context)