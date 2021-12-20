from django.shortcuts import redirect, render
from .models import BusinessEntity
from .forms import BusinessEntityForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

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
            messages.success(request, 'Company has been added!')
            context = {'all_entities': all_entities}
            return render(request, 'business_entities.html', context)
    else:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
        
        all_entities = BusinessEntity.objects.filter(
            Q(company_name__icontains=search_query) | Q(company_type__icontains=search_query) | Q(address__icontains=search_query) |
            Q(address2__icontains=search_query) | Q(city__icontains=search_query) | Q(region__icontains=search_query) |
            Q(postcode__icontains=search_query))
        context = {'all_entities': all_entities, 'search_query': search_query}
        return render(request, 'business_entities.html', context)

def business_entities_upd(request, company_name_id):
    all_entities = BusinessEntity.objects.get(pk=company_name_id)
    if request.method == 'POST':
        form = BusinessEntityForm(request.POST or None, instance = all_entities)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company has been updated!')
            return redirect('business_entities')
    else:
        context = {'all_entities': all_entities}
        return render(request, 'business_entities_upd.html', context)

def business_entities_del(request, company_name_id):
    all_entities = BusinessEntity.objects.get(pk=company_name_id)
    if request.method == 'POST':
        all_entities.delete()
        messages.success(request, 'Company has been deleted!')
        return redirect('business_entities')
    else:
        return render(request, 'business_entities_del.html')
