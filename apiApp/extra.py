# def index(request):
#     df = pd.read_csv('product_view.csv')
#     for i in range(df.shape[0]):
#         img = ['img1.png','img2.png','img3.png']
#         PRODUCT_NAME = list(df['name'])[i]
#         CATEGORY = list(df['category'])[i]
#         VARIENTS = list(df['sizes'])[i]
#         PRICE = list(df['price'])[i]
#         SIBLING_PRODUCT = list(df['sibling_product'])[i]
#         BENEFITS = list(df['benefits'])[i]
#         INGREDIENTS = list(df['ingredients'])[i]
#         HOW_TO_USE = list(df['how_to_use'])[i]
#         HOW_WE_MAKE_IT = list(df['how_we_make_it'])[i]
#         NUTRITIONAL_INFO = list(df['nutrition_info'])[i]
#         SKU_CODE = list(df['SKU'])[i]
#         HSN_CODE = list(df['HSN '])[i]

#         product = product_view.objects.values_list('PRODUCT_ID',flat=True)
#         PRODUCT_ID = 'RVP-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
#         check = True
#         while check:
#             if PRODUCT_ID not in product:
#                 product = product_view.objects.values_list('PRODUCT_ID',flat=True)
#                 check = False
#             else:
#                PRODUCT_ID = 'RVP-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))

#         VARIENT_ID = []
#         for j in SKU_CODE.split('|'):
#             prod_var = product_varient.objects.values_list('VARIENT_ID',flat=True)
#             varient = 'RVPV-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
#             check = True
#             while check:
#                 if varient not in prod_var:
#                     prod_var = product_varient.objects.values_list('VARIENT_ID',flat=True)
#                     check = False
#                 else:
#                     varient = 'RVPV-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
#             VARIENT_ID.append(varient)
#             p_v_data = product_varient(PRODUCT_ID = PRODUCT_ID,
#                                        VARIENT_ID = varient )
#             p_v_data.save()
#         VARIENT_ID = '|'.join(VARIENT_ID)    
#         CATEGORY_ID = list(category_view.objects.filter(CATEGORY_NAME = list(df['category'])[i]).values())[0]['CATEGORY_ID']
#         VARIENT_STOCK = '|'.join(list(['15']*len(SKU_CODE.split('|'))))
#         TOTAL_STOCK = sum(list(map(int, VARIENT_STOCK.split('|'))))
#         IMAGES = random.choice(img)

#         # print('PRODUCT_ID -',PRODUCT_ID,'\n')
#         # print('VARIENT_ID -',VARIENT_ID,'\n')
#         # print('PRODUCT_NAME -',PRODUCT_NAME,'\n')
#         # print('IMAGES -',IMAGES,'\n')
#         # print('CATEGORY_ID -',CATEGORY_ID,'\n')
#         # print('CATEGORY -',CATEGORY,'\n')
#         # print('VARIENTS -',VARIENTS,'\n')
#         # print('PRICE -',PRICE,'\n')
#         # print('VARIENT_STOCK -',VARIENT_STOCK,'\n')
#         # print('TOTAL_STOCK -',TOTAL_STOCK,'\n')
#         # print('SIBLING_PRODUCT -',SIBLING_PRODUCT,'\n')
#         # print('BENEFITS -',BENEFITS,'\n')
#         # print('INGREDIENTS -',INGREDIENTS,'\n')
#         # print('HOW_TO_USE -',HOW_TO_USE,'\n')
#         # print('HOW_WE_MAKE_IT -',HOW_WE_MAKE_IT,'\n')
#         # print('NUTRITIONAL_INFO -',NUTRITIONAL_INFO,'\n')
#         # print('SKU_CODE -',SKU_CODE,'\n')
#         # print('HSN_CODE -',HSN_CODE,'\n')

#         data = product_view(
#                             PRODUCT_ID = PRODUCT_ID,
#                             VARIENT_ID = VARIENT_ID,
#                             PRODUCT_NAME = PRODUCT_NAME,
#                             IMAGES = IMAGES,
#                             CATEGORY_ID = CATEGORY_ID,
#                             CATEGORY = CATEGORY,
#                             VARIENTS = VARIENTS,
#                             PRICE = PRICE,
#                             VARIENT_STOCK = VARIENT_STOCK,
#                             TOTAL_STOCK = TOTAL_STOCK,
#                             SIBLING_PRODUCT = SIBLING_PRODUCT,
#                             BENEFITS = BENEFITS,
#                             INGREDIENTS = INGREDIENTS,
#                             HOW_TO_USE = HOW_TO_USE,
#                             HOW_WE_MAKE_IT = HOW_WE_MAKE_IT,
#                             NUTRITIONAL_INFO = NUTRITIONAL_INFO,
#                             SKU_CODE = SKU_CODE,
#                             HSN_CODE = HSN_CODE,
#                             )
#         data.save()
#         print(i)
#     return HttpResponse('Hello')


# def cat(request):
#     df = pd.read_csv('category.csv')

#     for i in range(df.shape[0]):
#         CATEGORY_ID = 'RVC-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))    
#         CATEGORY_NAME = list(df['category'])[i]
#         COLOR_CODE = list(df['color'])[i]
#         IMAGES = list(df['image'])[i]
#         print(CATEGORY_NAME)
#         print(COLOR_CODE)
#         print(IMAGES)
#         category = category_view.objects.values_list('CATEGORY_ID',flat=True)
#         check = True
#         while check:
#             if CATEGORY_ID not in category:
#                 category = category_view.objects.values_list('CATEGORY_ID',flat=True)
#                 check = False
#             else:
#                CATEGORY_ID = 'RVC-'+''.join(random.choices(string.ascii_uppercase + string.digits, k = 5)) 
#         print(CATEGORY_ID)
#         data = category_view(
#                             CATEGORY_ID = CATEGORY_ID,
#                             CATEGORY_NAME = CATEGORY_NAME,
#                             COLOR_CODE = COLOR_CODE,
#                             IMAGES = IMAGES
#                             )
#         data.save()
#         print(i)
#     return HttpResponse('Hello')


# def index(request):
#     img_list = product_view.objects.values_list('PRODUCT_ID','SIBLING_PRODUCT')
#     for i in img_list:
#         p_id = product_view.objects.filter(PRODUCT_NAME = i[1]).values_list('PRODUCT_NAME','PRODUCT_ID')
#         product_view.objects.filter(PRODUCT_ID = i[0]).update(SIBLING_PRODUCT = p_id[0][1])
#         print()
        
#     return HttpResponse('hello')