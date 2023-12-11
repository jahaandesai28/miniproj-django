from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    path('',views.HomeView.as_view(),name='home'),
    path('about/',views.AboutView.as_view(),name='about'),
    # path('contact/',views.ContactView.as_view(),name='contact'),
    path('cart/',views.CartView.as_view(),name='cart'),
    path('add-to-cart/<int:pk>/',views.AddToCartView.as_view(),name='add-to-cart'),
    path('remove-from-cart/<int:pk>/',views.RemoveFromCartView.as_view(),name='remove-from-cart'),
]
