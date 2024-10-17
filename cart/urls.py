from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login'),
	path('logout/', views.logoutView, name='logout'),
	path('', views.product_list, name='product_list'),
	path('home', views.product_list, name='home'),
	path('cart/', views.view_cart, name='view_cart'),
	path('buy_now/<int:product_id>/', views.buy_now, name='buy_now'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
