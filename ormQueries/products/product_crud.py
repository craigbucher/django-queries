from .models import Product
from django.db import models
from datetime import datetime 
from django.utils import timezone 

class ProductCrud:
    
    @classmethod
    def get_all_products(cls):
        return (Product.objects.all())

    @classmethod
    def find_by_model(cls, model_name):
        for product in Product.objects.all():
            if product.model == model_name:
                return product
        return('Product not found!')
    
    @classmethod
    def last_record(cls):
       return(Product.objects.last())

    @classmethod
    def by_rating(cls, rating):
        return Product.objects.filter(rating__exact = rating)

    @classmethod
    def by_rating_range(cls, low, high):
        return Product.objects.filter(rating__range=(low, high))

    @classmethod
    def by_rating_and_color(cls, rating, color):
        return Product.objects.filter(rating__exact = rating, color__exact = color)

    @classmethod
    def by_rating_or_color(cls, rating, color):
        return Product.objects.filter(rating__exact = rating) | Product.objects.filter(color__exact = color)

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__exact = None).count()    