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


@api_view(['POST'])
def adminProductDetail(request):
    product_name = (request.data)['product']
    prod_obj = product_view.objects.filter(PRODUCT_NAME = product_name)\
                                   .values('PRODUCT_ID')\
                                   .annotate(
                                            name = F('PRODUCT_NAME'),
                                            slide = F('IMAGES'),
                                            size = F('VARIENTS'),
                                            price = F('PRICE'),
                                            benefits =F('BENEFITS'),
                                            ingredients =F('INGREDIENTS'),
                                            htu =F('HOW_TO_USE'),
                                            hwmi =F('HOW_WE_MAKE_IT'),
                                            nut_info =F('NUTRITIONAL_INFO'),
                                            nut_unit = F('NUTRITIONAL_UNIT'),
                                            stock = F('TOTAL_STOCK'),
                                            category = F('CATEGORY'),
                                            hsn = F('HSN_CODE'),
                                            sku = F('SKU_CODE'),
                                            varient_stock = F('VARIENT_STOCK'),
                                            sibling = F('SIBLING_PRODUCT')
                                            )
    prod_df = pd.DataFrame(list(prod_obj))
    prod_df['size'] = prod_df['size'].str.split('|')
    prod_df['price'] = prod_df['price'].str.split('|')
    prod_df['slide'] = prod_df['slide'].str.split('|')
    prod_df['nut_info'] = prod_df['nut_info'].str.split('|')
    prod_df['nut_unit'] = prod_df['nut_unit'].str.split('|')
    prod_df['sku'] = prod_df['sku'].str.split('|')
    prod_df['varient_stock'] = prod_df['varient_stock'].str.split('|')

    prod_df['benefits'] = prod_df['benefits'].str.replace('|',',',regex=True)
    prod_df['ingredients'] = prod_df['ingredients'].str.replace('|',',',regex=True)
    prod_df['htu'] = prod_df['htu'].str.replace('|',',',regex=True)
    prod_df['hwmi'] = prod_df['hwmi'].str.replace('|',',',regex=True)
    
    prod_df = prod_df.to_dict(orient='records')[-1]

    res = {}
    res['name'] = prod_df['name']
    res['status'] = 'In stock' if prod_df['stock']>0 else 'Out of stock'
    res['category'] = prod_df['category']
    res['hsn'] = prod_df['hsn']
    res['statusList'] = ["Out of stock", "In stock"]
    res['categoryList'] = category_view.objects.values_list('CATEGORY_NAME',flat=True)
    varients = []
    for i in range(len(prod_df['size'])):
        varients.append({
          'variantName': prod_df['size'][i],
          'price': prod_df['price'][i],
          'quantity': prod_df['varient_stock'][i],
          'sku':prod_df['sku'][i],
        }),
        res['variants'] = varients
    sibling = list(product_view.objects.filter(PRODUCT_ID = prod_df['sibling'])\
                                 .annotate(
                                            name = F('PRODUCT_NAME'),
                                            price = F('PRICE'),
                                            images = F('IMAGES')  
                                          )\
                                 .values('name','price','images'))[-1]
    res['sibling_product'] = {
                              'name':sibling['name'],
                              'price':sibling['price'],
                              'images':sibling['images'].split('|')[0]
                              }
    nutritional_info = []
    for i in range(len(prod_df['nut_info'])):
      if i==0:
        label = "Total fat"
      elif i==1:
        label = "Protien"
      elif i==2:
        label = "Carbohydrates"
      elif i==3:
        label = "Energy"
      nutritional_info.append({
          'label': label,
          'value': prod_df['nut_info'][i],
          'unit':  prod_df['nut_unit'][i],
      })
    res['nutritional_info'] = nutritional_info
    meta_field = [
                  {
                    'label':"How we make it?",
                    'desc':prod_df['hwmi']
                  },
                  {
                    'label':"How to use?",
                    'desc':prod_df['htu']
                  },
                  {
                    'label':"Ingredients",
                    'desc':prod_df['ingredients']
                  },
                  {
                    'label':"What's in it for you?",
                    'desc':prod_df['benefits']
                  },
                  ]
    res['meta_field'] = meta_field
    reviews =  [
      {
        'cust_name': "John Doe",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },

      {
        'cust_name': "Alex Bing",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "Ross Gellar",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "John Doe",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },

      {
        'cust_name': "Alex Bing",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "Ross Gellar",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "John Doe",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },

      {
        'cust_name': "Alex Bing",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "Ross Gellar",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "John Doe",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },

      {
        'cust_name': "Alex Bing",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
      {
        'cust_name': "Ross Gellar",
        'review': "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Fugiat velit atque labore laboriosam. Deserunt accusantium fugit vero dolorum assumenda minus nobis cumque sequi quas qui, tempore, nisi aperiam debitis, quo itaque ",
      },
    ]
    res['productList'] = product_view.objects.values_list('PRODUCT_NAME',flat=True)
    res['reviews'] = reviews
    return Response(res)