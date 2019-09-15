from django.shortcuts import render
from django.http import HttpResponse
from .models import Accounts
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.forms.models import model_to_dict
from .serializers import AccountsSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)


def getAccounts(request):
    c=Accounts.objects.all()
    d=AccountsSerializer(c, many=True)
    return JSONResponse(d.data)
