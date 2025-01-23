from django.shortcuts import render, redirect
from django.db.models import F
from .models import Product, CartItem, Order

def redirect_to_products(request):
    return redirect('/placeorder/browse')

def browse_products(request):
    cart_items = CartItem.objects.all()
    products = Product.objects.all()

    if request.method == 'POST':
        data = request.POST
        item_id = data.get('add_to_cart', None)
        if item_id:
            product = Product.objects.get(id=item_id)
            order = Order.objects.get(customer_name='Rohit')
            try:
                cart_item = CartItem.objects.get(product=product)
                cart_item.qty = F("qty") + 1
                cart_item.save()

            except Exception as e:
                cart_item = CartItem(order=order, product=product, qty=1)  
                cart_item.save()
            
        redirect('/placeorder/browse')

    context = {
        "products": products,
        "cart": cart_items
    }
    return render(request, 'placeorder/browse_products.html', context)