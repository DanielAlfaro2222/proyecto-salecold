from django import template
from Products.models import Product

register = template.Library()

@register.filter()
def discount_price(value):
    product = Product.objects.get(pk = value)
    price = product.unit_price
    discount = product.discount
    result = round(abs(price * (discount / 100) - price))
    return f'${result}'