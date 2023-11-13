from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'stockinfo/index2.html')

def pharmacies1(request):
    pharmacy = Pharmacy.objects.all()
    return render(request, "stockinfo/pharmacy.html", {
        'var_ph': pharmacy,
    })

def medicines1(request):
    medicine = Medicine.objects.all()
    return render(request, "stockinfo/medicine.html", {
        'var_med': medicine,
    })

def stocks(request):
    stock = Stock.objects.all()
    return render(request, "stockinfo/stock.html", {
        'var_stock' : stock,
    })