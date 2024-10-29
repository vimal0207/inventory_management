from django.db import models

class ActiveManager(models.Manager):
    """
    Custom manager to return only non-deleted records.
    """
    def get_queryset(self):
        # Override the default queryset to filter out soft-deleted items
        return super().get_queryset().filter(is_deleted=False)

class DeletedManager(models.Manager):
    """
    Custom manager to return only deleted records.
    """
    def get_queryset(self):
        # Override the default queryset to filter only soft-deleted items
        return super().get_queryset().filter(is_deleted=True)

class BaseModel(models.Model):
    """
    Abstract base model that includes fields for tracking creation and update timestamps,
    as well as a soft delete mechanism using the is_deleted field.
    """
    created_at = models.DateTimeField(auto_now_add=True)  
    # Automatically set to now when the object is created

    updated_at = models.DateTimeField(auto_now=True)  
    # Automatically set to now every time the object is saved (updated)

    is_deleted = models.BooleanField(default=False)
    # Flag to mark if the object is soft-deleted

    # Default manager to filter out soft-deleted records
    objects = ActiveManager()  
    # Additional manager to access all records, including soft-deleted ones
    all_objects = DeletedManager()  

    def delete(self, using=None, keep_parents=False):
        """
        Soft delete the object by setting is_deleted to True.
        """
        self.is_deleted = True
        # Save the updated state to the database
        self.save(using=using)

    def hard_delete(self, using=None, keep_parents=False):
        """
        Permanently delete the object from the database.
        """
        super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        """
        Meta class to specify that this is an abstract model,
        meaning no table will be created for it in the database.
        """
        abstract = True
