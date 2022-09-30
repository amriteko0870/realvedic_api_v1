from pyexpat import model
from tkinter import image_names
from django.db import models

# Create your models here.

class product_view(models.Model):
    PRODUCT_ID = models.CharField(max_length=300)
    VARIENT_ID = models.CharField(max_length=300)
    PRODUCT_NAME = models.CharField(max_length=300)
    IMAGES = models.CharField(max_length=300)
    CATEGORY_ID = models.CharField(max_length=300)
    CATEGORY =  models.CharField(max_length=300)
    VARIENTS = models.CharField(max_length=300)
    PRICE = models.CharField(max_length=300)
    VARIENT_STOCK = models.CharField(max_length=300)
    TOTAL_STOCK = models.IntegerField()
    SIBLING_PRODUCT = models.CharField(max_length=300)
    BENEFITS = models.TextField()
    INGREDIENTS = models.TextField()
    HOW_TO_USE = models.TextField()
    HOW_WE_MAKE_IT = models.TextField()
    NUTRITIONAL_INFO = models.TextField()
    NUTRITIONAL_UNIT = models.TextField()
    SKU_CODE = models.CharField(max_length=300) #varient_level
    HSN_CODE = models.CharField(max_length=300) #product_level


class product_varient(models.Model):
    PRODUCT_ID = models.CharField(max_length=300)
    VARIENT_ID = models.CharField(max_length=300)

class batch_account(models.Model):
    PRODUCT_ID = models.CharField(max_length=300)
    VARIENT_ID = models.CharField(max_length=300)
    BATCH_ID = models.CharField(max_length=300)
    BATCH_STOCK = models.IntegerField()
    BATCH_NUMBER = models.IntegerField()

class category_view(models.Model):
    CATEGORY_ID = models.CharField(max_length=300)
    CATEGORY_NAME = models.CharField(max_length=300)
    COLOR_CODE = models.CharField(max_length=300)
    IMAGES = models.CharField(max_length=300)

class log_records(models.Model):
    log_time = models.CharField(max_length=300)
    admin_name = models.CharField(max_length=300)
    changes_type = models.CharField(max_length=300)
    changes_details = models.CharField(max_length=300)

