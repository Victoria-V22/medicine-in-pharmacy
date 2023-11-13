from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class pharmacyAdmin(admin.ModelAdmin):
    list_display = ('address', 'number', 'metro_station')
    search_fields = ('address', 'metro_station')

admin.site.register(Pharmacy, pharmacyAdmin)

class medicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'quantity', 'manufacturer', 'prescription_required', 'category', 'price')
    list_filter = ('prescription_required', 'category')
    search_fields = ('name', 'manufacturer', 'category__name')

admin.site.register(Medicine, medicineAdmin)

class stockAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'medicine', 'quantity')
    list_filter = ('pharmacy', 'medicine')
    search_fields = ('pharmacy__address', 'medicine__name')

admin.site.register(Stock, stockAdmin)