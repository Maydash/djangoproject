from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('about_us/', views.about_us, name='about_us'),
    path('<int:products_id>/', views.product_detail, name='product_detail'),
    path('', views.index, name='index'),
]