from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('deta/<int:proid>/',views.detal,name='detal'),
    path('cate/<int:catid>',views.cate,name='cate'),
    path('add/<int:proid>/',views.add,name='add'),
    path('cart/',views.cartitem,name='cartitem'),
    path('delete/<int:proid>/',views.delet,name='delet'),
]