from django.contrib import admin
from .models import Dealer


class DealerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'brand', 'city',)
    list_filter = ('brand', 'city')
    fields = ['brand', 'company_name', 'url', 'phone', ('city', 'address', 'coordinates')]


admin.site.register(Dealer, DealerAdmin)
