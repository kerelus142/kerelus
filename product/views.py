from django.shortcuts import render,redirect
from .models import product, category,cart
# Create your views here.


def home(request):
    return render(request, 'index.html', {'pro': product.objects.all(),'item':cart.objects.all().count(), 'cat': category.objects.all()})


def cate(request, catid):
    return render(request, 'index.html', {'pro': product.objects.all().filter(category_id=catid), 'cat': category.objects.all(),'item':cart.objects.all().count()})


def detal(request, proid):
    return render(request, 'product_detail.html', {'pro': product.objects.all().filter(id=proid), 'cat': category.objects.all(),'item':cart.objects.all().count()})

def cartitem(request):
    return render(request, 'cart.html', {'pro': product.objects.all(),'cars':cart.objects.all() ,'cat': category.objects.all(),'item':cart.objects.all().count()})


def add(request,proid):
    a=int(cart.objects.filter(pri=proid).count())
    if a >= 1:
        s=cart.objects.get(pri=proid)
        cart.objects.filter(pri=proid).update(num=int(s.num)+1)
    else:
        carts=cart(pri=proid,num=1)
        carts.save()
    return redirect("/")

def delet(request,proid):
    a=int(cart.objects.filter(pri=proid).count())
    if a!=0:
        q=cart.objects.get(pri=proid)
        if q.num >1:
            cart.objects.filter(pri=proid).update(num=int(q.num)-1)
        
        else:
            q.delete()
    return redirect("/cart/")