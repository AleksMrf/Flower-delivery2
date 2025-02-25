from django.shortcuts import render, get_object_or_404
from .models import Flower

def catalog_home(request):
    flowers = Flower.objects.all()
    return render(request, 'catalog/list.html', {'flowers': flowers})

def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'catalog/detail.html', {'flower': flower})
