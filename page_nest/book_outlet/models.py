from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta :
        abstract=True

class Book(BaseModel) :
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    rating = models.IntegerField()
    