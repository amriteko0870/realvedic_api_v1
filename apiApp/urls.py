from operator import index
from django.urls import path
import apiApp.views as views
import apiApp.admin_views as ad_views



from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('adminProductList',ad_views.adminProductList,name='adminProductList'),
]


urlpatterns = [
    
]+admin_urls\
 +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
