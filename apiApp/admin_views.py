#--------------------------- django modules ----------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F

#---------------------------- python modules ---------------------------------------------
import pandas as pd

#---------------------------- django models ----------------------------------------------
from apiApp.models import category_view, product_varient, product_view,batch_account

#---------------------------- django rest modules ----------------------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response


# -------------------------- django views ------------------------------------------------

@api_view(['POST'])
def adminProductList(request,format=None):
    filter_data = (request.data)['data']
    print('################',filter_data)
    product_list = product_view.objects.all()\
                                       .values('id')\
                                       .annotate(
                                                 product_id = F('PRODUCT_ID'),
                                                 product_name = F('PRODUCT_NAME'),
                                                 category_id  =F('CATEGORY_ID'),
                                                 category = F('CATEGORY'),
                                                 varients_id  =F('VARIENT_ID'),
                                                #  varients = F('VARIENTS'),
                                                #  price = F('PRICE'),
                                                #  varient_stock = F('VARIENT_STOCK'),
                                                 total_stock = F('TOTAL_STOCK'),
                                                 hsn = F('HSN_CODE'),
                                                #  sku = F('SKU_CODE'),
                                                 image = F('IMAGES')
                                       )
    return Response(product_list)