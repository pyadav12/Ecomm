from django import template
register= template.Library()

@register.filter(name="is_exit_in_cart")
def is_exit_in_cart(product,cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
         return True
    return False


@register.filter(name="cart_quantity")
def cart_quantity(product,cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
         return cart.get(key)
    return False

@register.filter(name="total_price")
def total_price(product,cart):
   tp = product.price * cart_quantity(product,cart)
   
   return tp


@register.filter(name="pay_amount")
def pay_amount(product,cart):
    sum =0
    for i in product:
       sum =sum + total_price(i,cart)
   
    return sum
@register.filter(name="order_total_price")
def order_total_price(price,quantity):
   return price*quantity




