from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, default = "")
    price = models.FloatField(null = False)
    salePrice = models.FloatField()
    description = models.TextField()
    isActive = models.BooleanField(null = False)
    createdAt = models.DateField(auto_now_add = True)
    modifyAt = models.DateField(auto_now = True)
    thumbnail = models.TextField(null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    class Meta:
        app_label = "product"
        db_table = "product"
       