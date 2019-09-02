from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
	path('view_cart', views.view_cart, name='view_cart'),

]