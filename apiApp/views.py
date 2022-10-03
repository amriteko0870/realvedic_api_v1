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

def index(request):
    category_view.objects.filter(CATEGORY_ID__in = ['RVC-29UEZ','RVC-QLQ59','RVC-B50IK']).update(HSN_CODE = '9100000')
    category_view.objects.filter(CATEGORY_ID__in = ['RVC-YQALM']).update(HSN_CODE = '11010000')
    category_view.objects.filter(CATEGORY_ID__in = ['RVC-VP3YX']).update(HSN_CODE = '19024000')
    category_view.objects.filter(CATEGORY_ID__in = ['RVC-HEGTG']).update(HSN_CODE = '21060000')
    category_view.objects.filter(CATEGORY_ID__in = ['RVC-24MC3']).update(HSN_CODE = '21069099')
    return HttpResponse('Hello')