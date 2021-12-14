from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def contracts(request):
    return render(request, 'contracts.html',{})

def external_companies(request):
    return render(request, 'external_companies.html',{})

def internal_companies(request):
    return render(request, 'internal_companies.html',{})