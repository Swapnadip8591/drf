from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    """
    A simple API view that returns a JSON response.
    """
    #request is instance of HttpRequest
    
    print(request.GET)
    
    body = request.body  #raw bytes of Json data
    data={}
    try:
        data = json.loads(body)  #convert bytes to Python dict
    except:
        pass
    # print(data.keys())
    data['headers'] = dict(request.headers)  #convert headers to dict
    data['content_type'] = request.content_type  #content type of the request
    data['params'] = request.GET  #query parameters from the URL
 
    return JsonResponse(data)