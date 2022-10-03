from django.urls import path
import apiApp.views as views
import apiApp.admin_views as ad_views
import apiApp.user_views as us_views



from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('adminProductList',ad_views.adminProductList,name='adminProductList'),
    path('adminProductDetail',ad_views.adminProductDetail,name='adminProductDetail'),
    path('adminProductUpdate',ad_views.adminProductUpdate,name='adminProductUpdate'),
    
]

user_urls = [
    path('landingPage',us_views.landingPage,name='landingPage'),
    path('categoryPage',us_views.categoryPage,name='categoryPage'),
    path('productPage',us_views.productPage,name='productPage'),
]


urlpatterns = [
        path('',views.index,name='index')
]+admin_urls\
 +user_urls\
 +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
