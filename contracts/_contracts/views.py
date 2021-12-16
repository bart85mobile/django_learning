from django.shortcuts import render
from .models import BusinessEntity
from .forms import BusinessEntityForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html',{})

def contracts(request):
    return render(request, 'contracts.html',{})

def business_entities(request):
    if request.method == 'POST':
        form = BusinessEntityForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_entities = BusinessEntity.objects.all
            messages.success(request, 'Company has been added to the list!')
            return render(request, 'business_entities.html',{'all_entities': all_entities})
    else:
        all_entities = BusinessEntity.objects.all
        return render(request, 'business_entities.html',{'all_entities': all_entities})