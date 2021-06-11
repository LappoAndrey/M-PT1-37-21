from django.contrib import admin
from .models import LampType1,LampType2,LampType3, SelfDescription


admin.site.register(SelfDescription)
admin.site.register(LampType1)
admin.site.register(LampType2)
admin.site.register(LampType3)

# Register your models here.
