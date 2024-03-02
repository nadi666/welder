from django.shortcuts import render, redirect
from .models import Product
from .forms import CatalogForm

# main 
def home(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def product_list(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            catalog_id = form.cleaned_data['catalog']
            products = Product.objects.filter(catalog__id=catalog_id)
    else:
        form = CatalogForm()
        products = Product.objects.all()
    return render(request, 'main/menu.html', {'form': form, 'products': products})