from django.shortcuts import redirect, render
from .models import BusinessEntity
from .forms import BusinessEntityForm
from django.contrib import messages
from django.http import HttpResponseRedirect

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
            return render(request, 'business_entities.html', {'all_entities': all_entities})
    else:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
        
        all_entities = BusinessEntity.objects.filter(company_name__icontains=search_query)
        return render(request, 'business_entities.html', {'all_entities': all_entities})

def business_entities_delete(request, company_name_id):
    business_entity_delete = BusinessEntity.objects.get(pk=company_name_id)
    business_entity_delete.delete()
    messages.success(request, 'Company has been deleted!')
    return redirect('business_entities')

def business_entities_edit(request, company_name_id):
    if request.method == 'POST':
        all_entities = BusinessEntity.objects.get(pk=company_name_id)
        form = BusinessEntityForm(request.POST or None, instance = all_entities)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company has been updated!')
            return redirect('business_entities')
    else:
        all_entities = BusinessEntity.objects.get(pk=company_name_id)
        return render(request, 'business_entities_edit.html',{'all_entities': all_entities})
