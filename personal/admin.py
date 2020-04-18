from django.contrib import admin

# Register your models here.
from personal.models import Goods, Category

admin.site.register(Goods)
admin.site.register(Category)