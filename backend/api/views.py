from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view


'''
The whole django stuff managing json and http responses
'''
# def api_home(request, *args, **kwargs):
#     """
#     A simple API view that returns a JSON response.
#     """
#     #request is instance of HttpRequest
    
#     # print(request.GET)
    
#     # body = request.body  #raw bytes of Json data
#     # data={}
#     # try:
#     #     data = json.loads(body)  #convert bytes to Python dict
#     # except:
#     #     pass
#     # # print(data.keys())
#     # data['headers'] = dict(request.headers)  #convert headers to dict
#     # data['content_type'] = request.content_type  #content type of the request
#     # data['params'] = request.GET  #query parameters from the URL
    
#     '''
#     Fetch data from Models
#     '''
#     models_data = Product.objects.all().order_by("?").first()
#     data={}
#     if models_data:   
#         '''serialization --> model instance(models_data) to python dict and return json to client'''
#         # data['id'] = models_data.id
#         # data['title'] = models_data.title
#         # data['content'] = models_data.content
#         # data['price'] = models_data.price
        
#         data = model_to_dict(models_data, fields=['id', 'title'])
#         data_toStr= json.dumps(data)
 
#     # return JsonResponse(data)
#     return HttpResponse(data_toStr, headers={"content_type": "application/json"})  #adding price is data will give error that 
#                                                                                    #decimal is not json serializable

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    '''
    DEF API view
    '''
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        # data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])  #will not show sale_price
        data = ProductSerializer(model_data).data  
    return Response(data)