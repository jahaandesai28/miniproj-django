from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products,Cart
from django.views import View
from django.db import models

# # Create your views here.
# def home(request):
#     return render(request,'home.html')

# def about(request):
#     return render(request,'about.html')

# def contact(request):
#     return render(request,'contact.html')

class HomeView(View):
    def get(self,request):
        products=Products.objects.all()
        #sum of Cart.price
        cart_total= Cart.objects.all().aggregate(models.Sum('price'))
        return render(request,'home.html',{'products':products,'cart_total':cart_total})
    
class AboutView(View):
    def get(self,request):
        return render(request,'about.html')
    
class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')  

class CartView(View):
    def get(self,request):
        cart=Cart.objects.all()
        cart_total= Cart.objects.all().aggregate(models.Sum('price'))

        return render(request,'cart.html',{'cart':cart, 'cart_total':cart_total})
    
class AddToCartView(View):
    def get(self,request,pk):
        product=Products.objects.get(pk=pk)
        existing=Cart.objects.filter(product=product)
        if existing.exists():
            cart=existing.first()
            cart.quantity+=1
            cart.price+=product.price
            cart.save()
        else:
            cart=Cart.objects.create(product=product,quantity=1,price=product.price)
            
        # cart=Cart.objects.create(product=product,quantity=1,price=product.price)
        return redirect(to='home')
    
class RemoveFromCartView(View):
    def get(self,request,pk):
        product=Products.objects.get(pk=pk)
        existing=Cart.objects.filter(product=product)
        if existing.exists():
            cart=existing.first()
            if cart.quantity>1:
                cart.quantity-=1
                cart.price-=product.price
                cart.save()
            else:
                cart.delete()
        return redirect(to='cart')