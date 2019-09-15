from django.shortcuts import render
from django.http import HttpResponse
from .models import Plans
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.forms.models import model_to_dict
from .serializers import PlanSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)


def getPlans(request):
    c=Plans.objects.all()
    print(c)
    d=PlanSerializer(c, many=True)
    # d = serializers.serialize("json", c)

    print(d.data)
    return JSONResponse(d.data)
