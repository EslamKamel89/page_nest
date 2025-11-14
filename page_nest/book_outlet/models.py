from __future__ import annotations

from typing import Optional

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta :
        abstract=True


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self)-> str :
        return f"{self.name} - {self.code}"

    class Meta :
        verbose_name_plural = 'Countries'


class Address(models.Model) :
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    city= models.CharField(max_length=50)

    def __str__(self)->str :
        return f"{self.street}, {self.city} - Postal Code: {self.postal_code}"

    class Meta :
        verbose_name_plural = 'Address Entries'


class Author(BaseModel) :
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100 )
    address = models.OneToOneField(Address , on_delete=models.CASCADE , related_name='author' , null=True)
    def full_name(self ):
        return f"{self.first_name} {self.last_name}"

    def __str__(self)->str :
        return self.full_name()

class Book(BaseModel) :
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    rating = models.IntegerField(validators=[
        MinValueValidator(1) ,
        MaxValueValidator(5)
    ])
    author = models.ForeignKey(Author , on_delete=models.CASCADE  , null=True , related_name='books')
    is_bestselling=models.BooleanField(default=True)
    slug = models.SlugField(default='' , blank=True , null=False , db_index=True)
    published_countries = models.ManyToManyField(Country , related_name='books') # type: ignore
    # def save(self , *args:Any , **kwargs: Any) -> None:
    #     self.slug = slugify(self.title)
    #     super().save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug]) # type: ignore

    def __str__(self)->str:
        return f"title:{self.title}, description:{self.description}, rating:{self.rating}, author:{self.author}, is_bestselling:{self.is_bestselling}"



