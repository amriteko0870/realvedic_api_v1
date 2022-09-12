from operator import index
from django.urls import path
import apiApp.views as views



from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('',views.index,name='index'),
    # path('cat',views.cat,name='cat'),
    
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
