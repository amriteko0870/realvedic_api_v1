#--------------------------- django modules ----------------------------------------------
from math import prod
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F,Case,CharField,IntegerField,Value as V
from django.db.models.functions import StrIndex,Substr,Cast

#---------------------------- python modules ---------------------------------------------
import pandas as pd

#---------------------------- django models ----------------------------------------------
from apiApp.models import category_view, product_varient, product_view,batch_account


#---------------------------- django rest modules ----------------------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response


# -------------------------- django views ------------------------------------------------
@api_view(['GET'])
def landingPage(request):

    banner_1 = ['media/banner/banner1.svg','media/banner/banner2.svg']
    banner_2 = ['media/banner/banner2.svg','media/banner/banner1.svg']

    prod_obj = product_view.objects.values('id').annotate(name = F('PRODUCT_NAME') ,
                                             weight = F('VARIENTS'),
                                             image = F('IMAGES'),
                                             price = F('PRICE'))
    prod_df = pd.DataFrame(list(prod_obj))
    prod_df['weight'] = prod_df['weight'].str.split('|').str[0]
    prod_df['price'] = prod_df['price'].str.split('|').str[0].astype(int)
    prod_res = prod_df.to_dict(orient='records')

    cat_obj = category_view.objects.values('id').annotate(
                                                          name = F('CATEGORY_NAME'),
                                                          color = F('COLOR_CODE'),
                                                          image = F('IMAGES'),
                                                        )
    testimonial = pd.read_csv('testimonial.csv')
    back_img = ['media/testimonial/back/blob1.svg',
                'media/testimonial/back/blob1.svg',
                'media/testimonial/back/blob1.svg',
                'media/testimonial/back/blob1.svg',]
    testimonial_res = []
    for i in range(testimonial.shape[0]):
        d={}
        d['content'] = list(testimonial['testimonial'])[i]
        d['front'] = 'media/testimonial/profile/rectangle.svg'
        d['back'] = random.choice(back_img)
        testimonial_res.append(d)

    res = {
            'banner_1':banner_1,
            'banner_2':banner_2,
            'category':cat_obj,
            'best_seller':prod_res,
            'testimonial':testimonial_res
          }
    return Response(res)



@api_view(['GET'])
def categoryPage(request,format=None):
    category = request.GET.get('category')

    if category == 'Shop All':
        cover = {
            'name': 'Shop All',
            'color' : '#C57963',
            'image': 'media/category/shop_all.svg',
                }
        prod_obj = product_view.objects.values('id').annotate(name = F('PRODUCT_NAME') ,
                                             weight = F('VARIENTS'),
                                             image = F('IMAGES'),
                                             price = F('PRICE'))
        prod_df = pd.DataFrame(list(prod_obj))
        prod_df['weight'] = prod_df['weight'].str.split('|').str[0]
        prod_df['price'] = prod_df['price'].str.split('|').str[0].astype(int)
        prod_res = prod_df.to_dict(orient='records')
        exp_more = []
    else:
        cover = list(category_view.objects.filter(CATEGORY_NAME = category)\
                                   .values('CATEGORY_ID')\
                                   .annotate(
                                             name = F('CATEGORY_NAME'),
                                             color = F('COLOR_CODE'),
                                             image = F('IMAGES'),
                                            ))[-1]

        prod_obj = prod_obj = product_view.objects.filter(CATEGORY_ID = cover['CATEGORY_ID'])\
                                                  .values('id').annotate(name = F('PRODUCT_NAME') ,
                                                                         weight = F('VARIENTS'),
                                                                         image = F('IMAGES'),
                                                                         price = F('PRICE'))
        prod_df = pd.DataFrame(list(prod_obj))
        prod_df['weight'] = prod_df['weight'].str.split('|').str[0]
        prod_df['price'] = prod_df['price'].str.split('|').str[0].astype(int)
        prod_res = prod_df.to_dict(orient='records')

        exp_more_obj = exp_more_obj = product_view.objects.exclude(CATEGORY_ID = cover['CATEGORY_ID'])\
                                                  .values('id').annotate(name = F('PRODUCT_NAME') ,
                                                                         weight = F('VARIENTS'),
                                                                         image = F('IMAGES'),
                                                                         price = F('PRICE'))
        exp_more_df = pd.DataFrame(list(exp_more_obj))
        exp_more_df['weight'] = exp_more_df['weight'].str.split('|').str[0]
        exp_more_df['price'] = exp_more_df['price'].str.split('|').str[0].astype(int)
        exp_more = exp_more_df.to_dict(orient='records')
        random.shuffle(exp_more)
        exp_more = exp_more[::-1][:6]
    
    res = {
        'cover': cover,
        'product':prod_res,
        'explore_more': exp_more
        }
    return Response(res)


@api_view(['GET'])
def productPage(request,format=None):
    product_name = request.GET.get('product')
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
                                            )
    prod_df = pd.DataFrame(list(prod_obj))
    prod_df['size'] = prod_df['size'].str.split('|')
    prod_df['price'] = prod_df['price'].str.split('|')
    prod_df['slide'] = prod_df['slide'].str.split('|')

    prod_df['benefits'] = prod_df['benefits'].str.replace('|',',',regex=True)
    prod_df['ingredients'] = prod_df['ingredients'].str.replace('|',',',regex=True)
    prod_df['htu'] = prod_df['htu'].str.replace('|',',',regex=True)
    prod_df['hwmi'] = prod_df['hwmi'].str.replace('|',',',regex=True)
    prod_df['nut_info'] = prod_df['nut_info'].str.split('|')
    prod_res = prod_df.to_dict(orient='records')
    prod_res = prod_res[-1]
    
    
    desc = [{
                'title':'Benefits',
                'content': prod_res['benefits']
            },
            {
                'title':'Ingredients',
                'content':prod_res['ingredients']
            },
            {
                'title':'How we use it?',
                'content':prod_res['htu']
            },
            {
                'title':'How we make it?',
                'content':prod_res['hwmi']
            }]
    nutritional_info = [
        {
          'title': "Total Fat",
          'value': prod_res['nut_info'][0],
        },
        {
          'title': "Protien",
          'value': prod_res['nut_info'][1],
        },
        {
          'title': "Carbohydrate",
          'value': prod_res['nut_info'][2],
        },
        {
          'title': "Energy",
          'value': prod_res['nut_info'][3],
        },
      ]

    exp_more_obj = exp_more_obj = product_view.objects.exclude(PRODUCT_ID = prod_res['PRODUCT_ID'])\
                                                  .values('id').annotate(name = F('PRODUCT_NAME') ,
                                                                         weight = F('VARIENTS'),
                                                                         image = F('IMAGES'),
                                                                         price = F('PRICE'))
    exp_more_df = pd.DataFrame(list(exp_more_obj))
    exp_more_df['weight'] = exp_more_df['weight'].str.split('|').str[0]
    exp_more_df['price'] = exp_more_df['price'].str.split('|').str[0].astype(int)
    exp_more = exp_more_df.to_dict(orient='records')
    random.shuffle(exp_more)
    exp_more = exp_more[::-1][:6]

    res = {
        'name':prod_res['name'],
        'slide':prod_res['slide'],
        'size':prod_res['size'],
        'price':prod_res['price'],
        'desc':desc,
        'nutritional_info':nutritional_info,
        'explore_more':exp_more
          }

    return Response(res)