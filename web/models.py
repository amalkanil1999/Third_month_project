import uuid

from django.utils import timezone
  
from django.db import models


class Category(models.Model):
    section = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.section


class Tags(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    tags = models.ManyToManyField('web.Tags')

    is_deleted = models.BooleanField(default=False)
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to='product/')

    def __str__(self):
        return str(self.images)

    class Meta:
        verbose_name_plural = "images"