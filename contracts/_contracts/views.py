from django.shortcuts import redirect, render
from .models import ExternalEntity, InternalEntity, Contract
from .forms import ExternalEntityForm, InternalEntityForm, ContractForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

def home(request):
    return render(request, 'home.html',{})

def external_entities(request):
    if request.method == 'POST':
        form = ExternalEntityForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_entities = ExternalEntity.objects.all
            messages.success(request, 'Company has been added!')
            context = {'all_entities': all_entities}
            return render(request, 'external_entities.html', context)
    else:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
        
        all_entities = ExternalEntity.objects.filter(
            Q(company_name__icontains=search_query) | Q(address__icontains=search_query) |
            Q(address2__icontains=search_query) | Q(city__icontains=search_query) | Q(region__icontains=search_query) |
            Q(postcode__icontains=search_query))
        context = {'all_entities': all_entities, 'search_query': search_query}
        return render(request, 'external_entities.html', context)

def external_entities_upd(request, company_name_id):
    all_entities = ExternalEntity.objects.get(pk=company_name_id)
    if request.method == 'POST':
        form = ExternalEntityForm(request.POST or None, instance = all_entities)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company has been updated!')
            return redirect('external_entities')
    else:
        context = {'all_entities': all_entities}
        return render(request, 'external_entities_upd.html', context)

def external_entities_del(request, company_name_id):
    all_entities = ExternalEntity.objects.get(pk=company_name_id)
    if request.method == 'POST':
        all_entities.delete()
        messages.success(request, 'Company has been deleted!')
        return redirect('external_entities')
    else:
        return render(request, 'external_entities_del.html')

def internal_entities(request):
    if request.method == 'POST':
        form = InternalEntityForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_entities = InternalEntity.objects.all
            messages.success(request, 'Company has been added!')
            context = {'all_entities': all_entities}
            return render(request, 'internal_entities.html', context)
    else:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
        
        all_entities = InternalEntity.objects.filter(
            Q(company_name__icontains=search_query) | Q(address__icontains=search_query) |
            Q(address2__icontains=search_query) | Q(city__icontains=search_query) | Q(region__icontains=search_query) |
            Q(postcode__icontains=search_query))
        context = {'all_entities': all_entities, 'search_query': search_query}
        return render(request, 'internal_entities.html', context)

def internal_entities_upd(request, company_name_id):
    all_entities = InternalEntity.objects.get(pk=company_name_id)
    if request.method == 'POST':
        form = InternalEntityForm(request.POST or None, instance = all_entities)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company has been updated!')
            return redirect('internal_entities')
    else:
        context = {'all_entities': all_entities}
        return render(request, 'internal_entities_upd.html', context)

def internal_entities_del(request, company_name_id):
    all_entities = InternalEntity.objects.get(pk=company_name_id)
    if request.method == 'POST':
        all_entities.delete()
        messages.success(request, 'Company has been deleted!')
        return redirect('internal_entities')
    else:
        return render(request, 'internal_entities_del.html')
    
    

def contracts(request):
    all_external = ExternalEntity.objects.all
    all_internal = InternalEntity.objects.all
    context = {'all_external': all_external, 'all_internal': all_internal}
    return render(request, 'contracts.html', context)

def contracts(request):
    if request.method == 'POST':
        form = ContractForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_contracts = Contract.objects.all
            messages.success(request, 'Company has been added!')
            context = {'all_contracts': all_contracts}
            return render(request, 'contracts.html', context)
    else:
        search_query = ''
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
            
        all_external = ExternalEntity.objects.filter(company_name__icontains=search_query)
        all_internal = InternalEntity.objects.filter(company_name__icontains=search_query)
        
        all_contracts = Contract.objects.filter(
            Q(contract_name__icontains=search_query) |
            Q(company_name__in=all_external) |
            Q(company_name__in=all_internal) |
            Q(contract_date__icontains=search_query) |
            Q(contract_extension__icontains=search_query))
        context = {'all_contracts': all_contracts, 'search_query': search_query}
        return render(request, 'contracts.html', context)