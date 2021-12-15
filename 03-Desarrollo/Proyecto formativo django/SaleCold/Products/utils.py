from .models import Product
import random

def random_products(product):
    productos = Product.objects.exclude(pk=product.id_product)
    max = abs(Product.objects.all().count() - 7)
    num = random.randint(1, max)

    return productos[num:num + 6]