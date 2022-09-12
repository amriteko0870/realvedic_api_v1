from django.contrib import admin
from apiApp.models import product_view,category_view,batch_account,product_varient
# Register your models here.

admin.site.register(product_view)
admin.site.register(category_view)
admin.site.register(batch_account)
admin.site.register(product_varient)
