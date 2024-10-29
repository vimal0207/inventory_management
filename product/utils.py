from .models import StockChange

def update_stock_change(product_id, quantity, reason, date):
    data = {
        "product_id" : product_id,
        "quantity_changed" : quantity,
        "date_of_change" : date,
        "reason" : reason
    }
    StockChange.objects.create(**data)