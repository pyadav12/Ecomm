from django.contrib import admin

# Register your models here.
from .models import *

class RegAdmin(admin.ModelAdmin):
    list_display =["first_name", "last_name","email"]
    list_filter = ['first_name','last_name']
    search_fields= ['first_name','last_name','email']

admin.site.register(Registration,RegAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)

