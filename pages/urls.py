from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
]
