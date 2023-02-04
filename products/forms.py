from django import forms
from products.models import Product

class AddProduct(forms.Form):

    title = forms.CharField(label="Наименование")
    price = forms.DecimalField(label="Цена", decimal_places=2, max_digits=6)
    description = forms.CharField(label="Описание")
    quantity = forms.IntegerField(label="В ниличии", min_value=0)

class AllProduct(forms.Form):

    title = forms.CharField(label="Наименование")
    price = forms.DecimalField(label="Цена", decimal_places=2, max_digits=6)


class ProductModelForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'quantity')