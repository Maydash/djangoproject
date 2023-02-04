from django.shortcuts import render
from products.models import Product
from main.forms import Login_form
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme



def index(request):
    quantity = Product.objects.order_by('-quantity')[:3]

    return render(request, 'main/index.html', locals())


def login_user(request):
    form = Login_form(request.POST)
    # if form.is_valid():
    #     login1 = form.cleaned_data['login']
    #     password = form.cleaned_data['password']
    #     user = authenticate(request, username=login1, password=password)
    #     if user is not None:
    #         login(request, user)
    # way = request.META.get('HTTP_REFERER')

    # if not url_has_allowed_host_and_scheme(url=way, host=request.get_host()):
    #     way = reverse('main:index')
    # return HttpresponseRedirect(way)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, '../products/product_detail.html', locals())


def about_us(request):
    return render(request, 'main/about_us.html')