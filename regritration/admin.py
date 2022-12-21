from django.contrib import admin
from .models import Reg


class RegritrationAdmin(admin.ModelAdmin):
    list_display = ('Sur_name', 'First_name', 'Middle_name')

    
# Register your models here.
admin.site.register(Reg, RegritrationAdmin)