from base.views import BaseAuthenticatedViewSet
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(BaseAuthenticatedViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
