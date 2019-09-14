from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200,
    db_index=True)
    slug = models.SlugField(max_length=200,
    unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
        args=[self.slug])
    def __str__(self):
        return self.name
        
    
class Product(models.Model):
    category = models.ForeignKey(Category,
                                related_name='products',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    feature1 = models.CharField(max_length=60,blank=False, default='Feature')
    feature2 = models.CharField(max_length=60,blank=False, default='Feature')
    feature3 = models.CharField(max_length=60,blank=False, default='Feature')
    feature4 = models.CharField(max_length=60,blank=False, default='Feature')
    feature5 = models.CharField(max_length=60,blank=False, default='Feature')
    model = models.CharField(max_length=30,blank=False, default='Feature')
    color = models.CharField(max_length=30,blank=False, default='Feature')
    price = models.IntegerField(blank="False")
    old_price = models.IntegerField(blank=True, default="")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def get_absolute_url(self):
        return reverse('shop:product_detail',
        args=[self.id, self.slug])
    def __str__(self):
        return self.name