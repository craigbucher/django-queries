from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from .models import Product
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length


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

    @classmethod
    def below_price_or_above_rating(cls, price, rating):
        return Product.objects.filter(price_cents__lt = price) | Product.objects.filter(rating__gt = rating) 

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.all().order_by('category', '-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls, name):
        return Product.objects.filter(manufacturer__icontains = name)

    @classmethod
    def manufacturer_names_for_query(cls, query): # also needs to be alphabetical
        return Product.objects.filter(manufacturer__icontains = query).order_by().values_list('manufacturer', flat = True)
    
    @classmethod
    def not_in_a_category(cls, category):
        return Product.objects.filter(~Q(category__icontains = category))

    @classmethod
    def limited_not_in_a_category(cls, category, limit):
        return Product.objects.filter((~Q(category__icontains = category)))[:limit]

    @classmethod
    def category_manufacturers(cls, category):
        return Product.objects.filter(category__exact = category).values_list('manufacturer', flat = True)
        
    @classmethod
    def average_category_rating(cls, category):
        return Product.objects.filter(category__exact = category).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.aggregate(Max('model'))

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.all().order_by(Length('model'))