from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.exceptions import PermissionDenied

class AccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        
        raise PermissionDenied({"message": "You do not have permission to perform this action.", "error" : "not_allowed"})
    
class BaseAuthenticatedViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, AccessPermission]
    pagination_class = PageNumberPagination

    authorization_header = openapi.Parameter(
        'Authorization',
        openapi.IN_HEADER,
        description="Bearer <token>",
        type=openapi.TYPE_STRING,
        required=True,
        default="Bearer "
    )


    def get_schema(self):
        """Helper method to return schema with the authorization header."""
        return swagger_auto_schema(
            manual_parameters=[self.authorization_header]
        )

    @swagger_auto_schema(
        manual_parameters=[authorization_header]
    )
    def list(self, request, *args, **kwargs):
        """List all items."""
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return self.handle_error(e)

    @swagger_auto_schema(
        manual_parameters=[authorization_header]
    )
    def create(self, request, *args, **kwargs):
        """Create a new item."""
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return self.handle_error(e)

    @swagger_auto_schema(
        manual_parameters=[authorization_header]
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific item."""
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return self.handle_error(e)

    @swagger_auto_schema(
        manual_parameters=[authorization_header]
    )
    def partial_update(self, request, *args, **kwargs):
        """Partially update an existing item."""
        try:
            return super().partial_update(request, *args, **kwargs)
        except Exception as e:
            return self.handle_error(e)
        
    @swagger_auto_schema(
        manual_parameters=[authorization_header]
    )
    def update(self, request, *args, **kwargs):
        """Update an existing item."""
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return self.handle_error(e)

    @swagger_auto_schema(
        manual_parameters=[authorization_header]
    )
    def destroy(self, request, *args, **kwargs):
        """Delete a specific item."""
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return self.handle_error(e)

    def handle_error(self, error):
        """Handle the error and return a formatted response."""
        error_message = str(error)
        return Response(
            {"error": error_message, "message": "Something went wrong"},
            status=status.HTTP_400_BAD_REQUEST
        )
