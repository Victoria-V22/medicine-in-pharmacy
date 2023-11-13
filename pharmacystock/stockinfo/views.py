from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from .models import *

# def index(request):
#     pharmacy = Pharmacy.objects.all()
#     medicine = Medicine.objects.all()
#     stock = Stock.objects.all()
#     return render(request, 'stockinfo/index2.html', {'pharmacy': pharmacy, 'medicine': medicine, 'stock': stock, })

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




# def pharmacies(request):
#     pharmacy = Pharmacy.objects.all()
#     return render(request, "stockinfo/pharmacy.html", {
#         'pharmacy': pharmacy,
#         })

# def pharmacies(request):
#     pharmacy = Pharmacy.objects.all()
#     stock = Stock.objects.all()
#     return render(request, "stockinfo/test2.html", {
#         'var_pharmacy': pharmacy,
#         })

# def medicines(request):
#     medicine = Medicine.objects.all()
#     return render(request, "stockinfo/medicine.html", {
#         'var_medicine': medicine,
#     })


