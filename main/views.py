import os
from django.http import Http404, JsonResponse, HttpResponse
from django.contrib.auth.models import User
import stripe
from django.shortcuts import get_object_or_404, render,redirect
from .models import Item
from dotenv import load_dotenv
from django.conf import settings



def index(request):
    items = Item.objects.all()
    return render(request, 'main/index.html', {'items':items})


def create_checkout_session(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        raise Http404('Item does not found')
    session = stripe.checkout.Session.create(
        line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': item.name,
        },
        'unit_amount': int(item.price * 100),
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/success/'
    )
    return JsonResponse({'id': session.id})



def item_detail(request,id):
    item = get_object_or_404(Item, pk=id)
    context = {
        'item':item,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'main/item_detail.html', context)


def success_page(request):
    return render(request, 'main/success.html')



    

