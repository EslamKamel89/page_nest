from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta :
        abstract=True

class Book(BaseModel) :
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    rating = models.IntegerField(validators=[
        MinValueValidator(1) ,
        MaxValueValidator(5)
    ])
    author= models.CharField(max_length=100 , null=True)
    is_bestselling=models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id]) # type: ignore

    def __str__(self)->str:
        return f"title:{self.title}, description:{self.description}, rating:{self.rating}, author:{self.author}, is_bestselling:{self.is_bestselling}"
