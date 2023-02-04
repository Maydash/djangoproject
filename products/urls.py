from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('', views.all_products, name='all_products'),
    path('group/', views.product_group, name='product_group'),
    path('add_product/', views.add_product, name='add_product'),
    path('thanks/', views.thanks, name='thanks'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name="delete_product"),

]