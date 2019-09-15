
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.views.decorators.csrf import csrf_exempt
import json
import random
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from users.models import UserProfile
from django.core.mail import send_mail



@csrf_exempt 
def login(request):
    print(json.loads(request.body))

    if request.method == 'POST':
        req=json.loads(request.body)
        username = req['username']
        password = req['password']
        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse(user.id)
            
        else:
            return HttpResponse("invalid")  

@csrf_exempt 
def resetpass(request):
    if request.method == 'POST':
        req=json.loads(request.body)
        email = req['email']
        newpass="asdfg189"
        user = UserProfile.objects.filter(email_address=email)
        if user is not None:  
            # u = User.objects.get(username=user.phone_number)
            # u.set_password(newpass)
            send_mail(
                'Password reset',
                'Hi user, \n\nYour new password is ' + newpass + '\n\n Regards,\n Voizfonica Support Team' ,
                'admin@voizfonica.com',
                [email],
                fail_silently=True,
            )
            # u.save()
            return HttpResponse("success")
        else:
            return HttpResponse("failure")  
    return HttpResponse("invalid")
 

# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponse("success")