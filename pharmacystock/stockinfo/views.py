from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'stockinfo/index2.html')

def pharmacies1(request):
    pharmacies_list = Pharmacy.objects.all()
    for pharmacy in pharmacies_list:
        pharmacy_medicines = Stock.objects.filter(pharmacy=pharmacy).select_related('medicine')
        pharmacy.medicines = [stock.medicine.name for stock in pharmacy_medicines]

    return render(request, "stockinfo/pharmacy2.html", {
        'var_ph': pharmacies_list,
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