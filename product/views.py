from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from base.views import BaseAuthenticatedViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import F, Sum

class ProductViewSet(BaseAuthenticatedViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Create a new product and log the stock change."""
        reason = serializer.validated_data.pop("reason")
        product = serializer.save()
        print(product.id)
        product.update_stock_change(reason)

    def perform_update(self, serializer):
        """Update an existing product and log the stock change."""
        product = self.get_object()
        old_quantity = product.quantity
        if "reason" in serializer.validated_data:
            reason = serializer.validated_data.pop("reason")
        else:
            reason = self.request.data.get('reason', 'Updated')
        updated_product = serializer.save()
        new_quantity = updated_product.quantity

        quantity_change = new_quantity - old_quantity
        if quantity_change != 0:
            updated_product.update_stock_change(reason, quantity_change)

    
    @swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Amount of stock to add'),
                'reason': openapi.Schema(type=openapi.TYPE_STRING, description='Reason for adding stock')
            },
            required=['quantity', 'reason']
        ),
        manual_parameters=[BaseAuthenticatedViewSet.authorization_header],
        responses={
            200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'message': openapi.Schema(type=openapi.TYPE_STRING), 'new_quantity': openapi.Schema(type=openapi.TYPE_INTEGER)})),
            400: openapi.Response('Bad Request', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
        }
    )
    @action(detail=True, methods=['post'], url_path='add-stock')
    def add_stock(self, request, pk=None):
        """Add stock to an existing product."""
        product = self.get_object()
        quantity = request.data.get('quantity', 0)
        reason = request.data.get('reason', 'Stock added')
        res_status, msg = product.add_stock(quantity, reason)
        if res_status:
            return Response({"message": "Stock added successfully.", }, status=status.HTTP_200_OK)
        return Response({"message": msg, "error": msg}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        method='post',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Amount of stock to remove'),
                'reason': openapi.Schema(type=openapi.TYPE_STRING, description='Reason for removing stock')
            },
            required=['quantity', 'reason']
        ),
        manual_parameters=[BaseAuthenticatedViewSet.authorization_header],
        responses={
            200: openapi.Response('Success', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'message': openapi.Schema(type=openapi.TYPE_STRING), 'new_quantity': openapi.Schema(type=openapi.TYPE_INTEGER)})),
            400: openapi.Response('Bad Request', openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
        }
    )
    @action(detail=True, methods=['post'], url_path='remove-stock')
    def remove_stock(self, request, pk=None):
        """Remove stock from an existing product."""
        product = self.get_object()
        quantity = request.data.get('quantity', 0)
        reason = request.data.get('reason', 'Stock removed')
        res_status, msg = product.remove_stock(quantity, reason)
        if res_status:
            return Response({"message": "Stock removed successfully.", }, status=status.HTTP_200_OK)
        return Response({"message": msg, "error": msg}, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(BaseAuthenticatedViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class InventoryReportView(APIView):
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('category', openapi.IN_QUERY, description='Filter by category', type=openapi.TYPE_STRING),
            openapi.Parameter('supplier', openapi.IN_QUERY, description='Filter by supplier', type=openapi.TYPE_STRING),
            openapi.Parameter('stock_level', openapi.IN_QUERY, description='Filter by stock level', type=openapi.TYPE_STRING),
            openapi.Parameter('sort', openapi.IN_QUERY, description='Sort order (asc/desc)', type=openapi.TYPE_STRING, required=False, default='asc'),
            BaseAuthenticatedViewSet.authorization_header
        ],
    )
    def get(self, request):
        category = request.query_params.get("category")
        supplier = request.query_params.get("supplier")
        stock_level = request.query_params.get("stock_level")
        sort_order = request.query_params.get("sort", "asc")

        queryset = Product.objects.all()
        if category:
            queryset = queryset.filter(category_id=category)
        if supplier:
            queryset = queryset.filter(supplier_id=supplier)
        if stock_level == "low":
            queryset = queryset.filter(quantity__lt=F("alert_threshold"))
        elif stock_level == "sufficient":
            queryset = queryset.filter(quantity__gte=F("alert_threshold"))

        if sort_order == "desc":
            queryset = queryset.order_by("-quantity")
        else:
            queryset = queryset.order_by("quantity")

        total_inventory_value = queryset.aggregate(
            total_value=Sum(F("quantity") * F("price"))
        )["total_value"] or 0

        serializer = ProductSerializer(queryset, many=True)
        
        data = {
            "total_inventory_value": total_inventory_value,
            "products": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)