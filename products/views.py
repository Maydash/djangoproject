from django.shortcuts import render, redirect
from products.models import Product, Group
from decimal import Decimal
from products.forms import ProductModelForm, AddProduct, AllProduct


def product_group(request):
    group = Group.objects.all()
    return render(request, 'products/product_group.html', locals())


def all_products(request):
    products = Product.objects.all()
    form = AllProduct()
    return render(request, 'products/all_products.html', locals())


def product_detail(request, id):
    product = Product.objects.get(id=id)
    form = ProductModelForm(instance=product)
    return render(request, 'products/product_detail.html', locals())


def add_product(request):
    form = AddProduct()
    return render(request, 'products/add_product.html', locals())


def thanks(request):
    title = request.POST['title']
    price = request.POST['price']
    quantity = request.POST['quantity']
    description = request.POST['description']
    p = Product(title=title, price=price, quantity=quantity, description=description)
    p.save()
    return render(request, 'products/thanks.html', locals())


def edit_product(request, id):
    if request.method == 'GET':
        product = Product.objects.filter(id=id).first()
        form = ProductModelForm(instance=product)
        # product.price = str(product.price)
        # p = Product(title=title, price=price, quantity=quantity, description=description)
        # p.save()
        return render(request, 'products/edit_product.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        price = Decimal(request.POST['price'])
        quantity = request.POST['quantity']
        description = request.POST['description']
        # p = Product(
        #     title=title, price=price, 
        #     quantity=quantity, description=description
        # )
        # Product.objects.update(id=id, title='aaaaaaa')
        #p.save()
        p = Product.objects.get(id=id)
        p.title = title
        p.price = price
        p.quantity = quantity
        p.description = description
        p.save()
        return redirect('products:all_products')


def delete_product(request, id):
    if request.method == 'GET':
        product = Product.objects.filter(id=id).first()
        form = ProductModelForm(instance=product)
        # product.price = str(product.price)
        # p = Product(title=title, price=price, quantity=quantity, description=description)
        # p.save()
        return render(request, 'products/delete_product.html', locals())
    elif request.method == 'POST':
        # title = request.POST['title']
        # price = Decimal(request.POST['price'])
        # quantity = request.POST['quantity']
        # description = request.POST['description']
        p = Product.objects.get(id=id)
        p.delete()
        return redirect('products:all_products')
    



