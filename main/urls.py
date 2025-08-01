from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:id>/', views.create_checkout_session, name='checkout'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('success/', views.success_page, name='success'),
    path('create-admin/', views.create_sepueruser),
]
