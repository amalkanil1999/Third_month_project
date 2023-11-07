from django.contrib import admin
from web.models import *


admin.site.register(Category)


admin.site.register(Tags)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','id','description',)

admin.site.register(Product,ProductAdmin)


admin.site.register(Images)


