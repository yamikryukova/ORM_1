from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_data = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }
    return render(request, 'catalog.html', {
        "phones": Phone.objects.all().order_by(
            sort_data.get(request.GET.get("sort"), "id")
        )
    })


def show_product(request, slug):
    template = 'product.html'
    context = {
        "phone": Phone.objects.get(slug=slug)
    }
    return render(request, template, context)
