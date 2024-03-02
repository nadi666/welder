from django import forms 
from django.conf import settings 
from .models import Catalog, Product


class CatalogForm(forms.Form):
    catalog = forms.ChoiceField(choices=[(c.id, c.name) for c in Catalog.objects.all()], widget=forms.Select)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'