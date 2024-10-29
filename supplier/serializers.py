from base.serializers import BaseSerializer
from .models import Supplier

class SupplierSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Supplier
