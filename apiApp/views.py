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

