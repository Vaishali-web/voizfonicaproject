from django.shortcuts import render
from django.http import HttpResponse
from .models import Connection
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.core.mail import send_mail
from django.forms.models import model_to_dict
from .serializers import ConnectionSerializer
from django.views.decorators.csrf import csrf_exempt
import json
import time
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework.parsers import JSONParser
import random
from django.contrib.auth.models import User
from accounts.models import Accounts,Proofs
from users.models import UserProfile
from plans.models import Plans, Costing


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def conn(request):
    if request.method == 'POST' and request.FILES['uploadFile']:
        myfile = request.FILES['uploadFile']
        fs = FileSystemStorage()
        filename = fs.save("uploads/proofs/" + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        inputUser=eval((request.POST["data"]))
        inputUser["proofFile"]=uploaded_file_url
        inputUser["requested_date_time"]=datetime.datetime
        inputUser["status"]="Initiated"
        
        if inputUser["portin"]=="True":
            portin=True
        else:
            portin=False

        # serializer = ConnectionSerializer(data=inputUser, many=True, context={"request":request})
        # print(serializer.is_valid())

        app_no = str(time.time()).replace(".","")
        c=Connection(application_number=app_no,first_name=inputUser['first_name'],last_name= inputUser['last_name'],city=inputUser['city'],state=inputUser['state'],zip=inputUser['zip'],email=inputUser['email'],password=inputUser['password'],proof=inputUser['proof'],proofnumber=inputUser['proofnumber'],address=inputUser['address'],portin=portin,current_mobile_number=inputUser['current_mobile_number'],current_network=inputUser['current_network'],upc=inputUser['upc'],status=inputUser['status'],circle=inputUser['circle'],connectiontype=inputUser['connectiontype'],proofFile=inputUser['proofFile'],dongleselected=inputUser['dongleselected'],requested_date_time='requested_date_time')
        c.save()

        send_mail(
        'Thank you for your choosing Voizfonica',
        'Hi ' + inputUser["first_name"] + ', \n\nWe have received your connection request. Soon you will recieve a mail once your request is approved and your dongle or simcard will be delivered to your requested address after approval. Your application number is ' + app_no,
        'admin@voizfonica.com',
        [inputUser['email']],
        fail_silently=True,
        )

        return JSONResponse("success")

def approve(request):
    if request.method == 'POST':
        print(request.POST["app_id"])
        v=Connection.objects.get(application_number = request.POST["app_id"])
        
        ph=str(random.randint(9000000000,9999999999))

        
        
        p=Plans.objects.filter(plans_name="base plan")
        for plan in p:
            plantobeadded = plan
        c=Costing(flags=False, calls='0', data='0', sms='0')
        pr=Proofs(proof=v.proofFile)
        pr.save()
        prooftobeadded = Proofs.objects.filter(_id=pr.pk).first()
        print(prooftobeadded)
        sAccount = Accounts(account_type=v.connectiontype,phone_number=ph, main_balance=0,expiry="2029-05-20",amount_due="0",payment_deadline="2029-05-20", circle=v.circle, imei="998988989898989",current_usage=c)
        sAccount.save()
        sAccount.plan_activated.add(plantobeadded)
        sAccount.proofs_attached.add(prooftobeadded)
        sAccount.save()

        send_mail(
        'Thank you for your choosing Voizfonica',
        'Hi ' + v.first_name + ', \n\nYour connection request has been approved. Your assigned phone number is \'' + ph + '\'. You can signup with this phone number and get started with voizfonica. Thank you for being a part of Voizfinica family.',
        'admin@voizfonica.com',
        [v.email],
        fail_silently=True,
        )


        return HttpResponse("success")

    
def displayhome(request):   
    a = Connection.objects.all()
    return render(request,"display.html",{'a':a })

@csrf_exempt
def individualfunction(request):
   
    if request.method == 'GET':
        a = Connection.objects.filter(application_number = request.GET.get("search2"))
        return render(request,"individualdetails.html",{'a':a })
