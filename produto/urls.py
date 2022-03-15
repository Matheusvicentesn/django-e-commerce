from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('addtocart/', views.AddToCart.as_view(), name='addtocart'),
    path('remove/', views.Remove.as_view(), name='remove'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('finish/', views.Finish.as_view(), name='finish'),

]
