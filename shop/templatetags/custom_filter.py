from django import template

register = template.Library()

@register.filter(name='rupee')
def addRupeeSign(value):
    return f'₹ {value}'



@register.filter(name='sale_price')
def addDiscount(obj):
    price = obj.price
    dis = obj.discount
    sale_price = price-(price*dis/100)
    return sale_price