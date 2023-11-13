from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

from django.shortcuts import render
from .models import *

def index(request):
    pharmacy = Pharmacy.objects.all()
    medicine = Medicine.objects.all()
    stock = Stock.objects.all()
    return render(request, 'stockinfo/index1.html', {'pharmacy': pharmacy, 'medicine': medicine, 'stock': stock, })

# def pharmacies(request):
#     pharmacies = Pharmacy.objects.all()
#     return render(request, "pharmacy/pharmacies.html", {
#         'var_pharmacies': pharmacies,
#     })

# def medicines(request):
#     medicines = Medicine.objects.all()
#     return render(request, "pharmacy/medicines.html", {
#         'var_medicines': medicines,
#     })

# def stocks(request):
#     stocks = Stock.objects.all()
#     return render(request, "pharmacy/stocks.html", {
#         'var_stocks': stocks,
#     })


