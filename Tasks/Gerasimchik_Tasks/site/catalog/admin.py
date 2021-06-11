from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand",)}


admin.site.register(Brand, BrandAdmin)
