from django.contrib import admin
from django import forms
from django.forms import ModelChoiceField
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CategoryChoiceField(forms.ModelChoiceField):
    pass


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(
                Category.objects.filter(slug='notebooks'))


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(
                Category.objects.filter(slug='smartphones'))


admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
