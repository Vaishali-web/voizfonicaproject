from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from plans.models import Plans
from accounts.models import Accounts
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json 
import datetime
from djongo.models.fields import ArrayReferenceManagerMixin



class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def getUser(request):
    if request.method == 'POST':
        
        inputData = json.loads(request.body)
        c=UserProfile.objects.filter(user=inputData["userid"])
        d=UserProfileSerializer(c, many=True)
        print(d.data)
        return JSONResponse(d.data)
        # return JSONResponse("")

@csrf_exempt
def doRegister(request):
    if request.method == 'POST' and request.FILES['uploadFile']:
        myfile = request.FILES['uploadFile']
        fs = FileSystemStorage()
        filename = fs.save("uploads/profile_pic/" + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        inputUser=eval((request.POST["data"]))

        checkExists = User.objects.filter(username=inputUser["phonenumber"])
        if checkExists.count() > 0:
            return JSONResponse("Already exists")

        dUser = User.objects.create_user(username=inputUser["phonenumber"], password=inputUser["password"], email=inputUser["email"])
        dUser.save()
        
        userNew = User.objects.get(id=dUser.pk)
        sUser = UserProfile(user=userNew, first_name = inputUser["firstname"],
        last_name = inputUser["lastname"] ,
        email_address = inputUser["email"],phone_number = inputUser["phonenumber"],alternate_phone = inputUser["phonenumber"], kyc_verified = False, profile_pic = uploaded_file_url, user_joined_date = datetime.date.today())

        sAccounts = Accounts.objects.filter(phone_number = inputUser["phonenumber"])
        if sAccounts.count() > 0:
            for account in sAccounts:
                sUser.accounts_linked.add(account)

        sUser.save()

        send_mail(
            'Thank you for choosing VoizFonica!',
            'Hi' + inputUser["firstname"] + ', \n\nWelcome to VoizFonica. We promise you the best services that includes voice and data services. We are the leading service providers in India and we have more than 1 Billion customers. Hope you will enjoy our services. If you are already a customer of voizfonica your existing accounts will be added to this user profile. For any queries, contact the chat support in the website.\n\n Regards,\n Voizfonica Support Team' ,
            'admin@voizfonica.com',
            ['skandagurunathan.iprimed@gmail.com'],
            fail_silently=True,
        )

        return JSONResponse("success")
    return JSONResponse("error")

@csrf_exempt
def changepassword(request):
    if request.method=='POST':
        inputData= json.loads(request.body)
        c=User.objects.filter(id=inputData["userid"])
        print(inputData)
        user = authenticate(username=c[0].username, password=inputData["oldpass"])
        if user is not None:  
            u = User.objects.get(username=c[0].username)
            u.set_password(inputData["newpass"])
            u.save()
            return HttpResponse("success")
        else:
            return HttpResponse("failure")  

@csrf_exempt
def usageSimulator(request):
    if request.method=="POST":
        return HttpResponse("")
    if request.method=="GET":
        if "userid" not in request.GET:
            u=UserProfile.objects.all().values()
            if  "account_phone" not in request.GET:
                return render(request, "usagesimulator.html", {"users": u})
        else:
            users=UserProfile.objects.filter(phone_number=request.GET["userid"])
            u=UserProfile.objects.get(phone_number=request.GET["userid"])
            accounts_phone=[]
            for account in users[0].accounts_linked_id:
                acc_type = Accounts.objects.filter(_id=account)
                accounts_phone.append(acc_type[0])
            if "account_phone" in request.GET:
                a=Accounts.objects.filter(phone_number=request.GET["account_phone"])
                plan_names=[]
                for plan in a[0].plan_activated_id:
                    p=Plans.objects.filter(_id=plan).values()
                    plan_names.append(p[0])
                if "plan_id" in request.GET:
                    acc=Accounts.objects.filter(phone_number=request.GET["account_phone"])
                    current_usage = acc[0].current_usage
                    
                    p=Plans.objects.filter(id=request.GET["plan_id"])
                    max_usage = p[0].value_delivered

                    if "calls" in request.GET:
                        acc=Accounts.objects.get(phone_number=request.GET["account_phone"])
                        acc.current_usage.calls= request.GET["calls"]
                        acc.current_usage.data= request.GET["data"]
                        acc.current_usage.sms= request.GET["sms"]
                        acc.save()
                        send_mail_fun(acc.current_usage, p[0].value_delivered, users[0].email_address, users[0].first_name)
                        acco=Accounts.objects.filter(phone_number=request.GET["account_phone"])
                        current_usage = acco[0].current_usage

                        return render(request, "usagesimulator.html", {"users": users, "accounts_phone": accounts_phone, "plan_name": plan_names, "current_usage": current_usage, "max_usage": max_usage})
                    else:
                        return render(request, "usagesimulator.html", {"users": users, "accounts_phone": accounts_phone, "plan_name": plan_names, "current_usage": current_usage, "max_usage": max_usage})
                else:
                    return render(request, "usagesimulator.html", {"users": users, "accounts_phone": a, "plan_name": plan_names})
            else:
                return render(request, "usagesimulator.html", {"users": users, "accounts_phone": accounts_phone})

def send_mail_fun(current, plan, email, first_name):
    if plan.data!="0":
        if(int(current.data)/int(plan.data)>=0.9):
            send_mail(
                'You have consumed 90 percent of data',
                'Hi ' + first_name + ', \n\nYou have consumed more than 90 percent of data as per your plan. Please recharge or upgrade plan to continue the benefits. For any queries, contact the chat support in the website.\n\n Regards,\n Voizfonica Support Team' ,
                'admin@voizfonica.com',
                [email],
                fail_silently=True,
            )
    if plan.data!="0":
        if(int(current.data)/int(plan.data)>=0.5):
            send_mail(
                'You have consumed 50 percent of data',
                'Hi' + first_name + ', \n\nYou have consumed more than 50 percent of data as per your plan. Please recharge or upgrade plan to continue the benefits.  For any queries, contact the chat support in the website.\n\n Regards,\n Voizfonica Support Team' ,
                'admin@voizfonica.com',
                [email],
                fail_silently=True,
            )
    if plan.calls!="0":
        if(int(current.calls)/int(plan.calls)>=0.9):
            send_mail(
                'You have consumed 90 percent of calls',
                'Hi  '  + first_name +', \n\nYou have consumed more than 90 percent of calls as per your plan. Please recharge or upgrade plan to continue the benefits.  For any queries, contact the chat support in the website.\n\n Regards,\n Voizfonica Support Team' ,
                'admin@voizfonica.com',
                [email],
                fail_silently=True,
            )
    if plan.sms!="0":
        print(current.sms + " " + plan.sms)
        if(int(current.sms)/int(plan.sms)>=0.9):
            send_mail(
                'You have consumed 90 percent of sms',
                'Hi '  + first_name +', \n\nYou have consumed more than 90 percent of sms as per your plan. Please recharge or upgrade plan to continue the benefits.  For any queries, contact the chat support in the website.\n\n Regards,\n Voizfonica Support Team' ,
                'admin@voizfonica.com',
                [email],
                fail_silently=True,
            )
