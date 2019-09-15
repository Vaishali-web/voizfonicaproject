from django.shortcuts import render
from django.http import HttpResponse
from .models import Offer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import OfferSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):

        #converting python primitive type to json data
        content= JSONRenderer().render(data)

        #adding 'content_type' key to the response header as 'application/json'
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def offer_list(request):
    if request.method == 'GET':

        #get all plans from db
        off = Offer.objects.filter(offers_to_users__in=[request.GET["userid"]])

        #convert python model data into python premitive using serializer
        off_serializer =  OfferSerializer(off, many = True)

        #return
        return JSONResponse(off_serializer.data)

    elif request.method == 'POST':
        off_data = JSONParser().parse(request)
        off_serializer = OfferSerializer(data=off_data)
        if Offer_serializer.is_valid():
            Offer_serializer.save()
            return JSONResponse(Offer_serializer.data,status=status.HTTP_201_CREATED)
        return JSONResponse(Offer_serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def offer_list2(request):
    if request.method == 'GET':
    
            #get all plans from db
        off = Offer.objects.all()
    
            #convert python model data into python premitive using serializer
        off_serializer =  OfferSerializer(off, many = True)
    
            #return
        return JSONResponse(off_serializer.data)
    
    elif request.method == 'POST':
        off_data = JSONParser().parse(request)
        off_serializer = OfferSerializer(data=off_data)
        if Offer_serializer.is_valid():
            Offer_serializer.save()
            return JSONResponse(Offer_serializer.data,status=status.HTTP_201_CREATED)
        return JSONResponse(Offer_serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
def offer_detail(request,pk):
    try: 
        off = Offer.objects.get(pk = pk)
    except Offer.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        off_serializer = OfferSerializer(off)
        return JSONResponse(off_serializer.data)
    
    elif request.method == "PUT":
        off_data = JSONParser().parse(request)
        off_serializer = OfferSerializer(off, data=off_data)
        if off_serializer.is_valid():
            off_serializer.save()
            return JSONResponse(off_serializer.data)
        return JSONResponse(off_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        off.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)









