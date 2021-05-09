from django.urls import path, include
from . import views

app_name = 'base'
urlpatterns = [
   path('',views.home,name='home'),
   path('index/',views.index,name='index'),
   path('charge/', views.charge, name="charge"),
   path('success/', views.success, name="success"),
   path('invoice/', views.invoice, name="invoice"),
   path('email/', views.email, name="email"),
]