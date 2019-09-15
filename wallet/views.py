from django.shortcuts import render
from django.http import HttpResponse
from .models import Wallet
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from .serializers import WalletSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import UserProfile

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def getWallet(request):
    if request.method=='GET':
        c=Wallet.objects.all()
        d=WalletSerializer(c, many=True)
        print(d.data)
        return JSONResponse(d.data)

    if request.method == 'POST':  
        j=json.loads(request.body)
        obj=Wallet(wallet_name=j['wallet_name'],wallet_auth_id=j['wallet_auth_id'],wallet_processing_charges=j['wallet_processing_charges'])
        obj.save()
        w=Wallet.objects.get(_id=obj.pk)
        us=UserProfile.objects.get(user_id=j["userid"])
        us.wallets_linked.add(w)
        us.save()
        return JSONResponse("success")


