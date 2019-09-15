from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.core import serializers
from .serializers import TicketSerializer,ChatSerializer,MessagesSerializer
from .models import Ticket,Chat,Messages
from users.models import UserProfile
import json
import datetime

#from django.contrib.auth.decorators import login_required
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

class JSONResponse(HttpResponse):
     def __init__(self,data,**kwargs):
          content=JSONRenderer().render(data)
          kwargs['content_type']='application/json'
          super(JSONResponse,self).__init__(content,**kwargs)

#@login_required
@csrf_exempt
def ticket(request):
     if request.method=='GET':
          TicketBC=Ticket.objects.all()
          TicketAC=TicketSerializer(TicketBC,many=True)
          print(TicketAC)
          return JSONResponse(TicketAC.data)
     
     if request.method=='POST':
          j=json.loads(request.body)
          obj=Ticket(ticket_id=j['ticket_id'],ticket_type=j["ticket_type"],ticket_issue_date=j["ticket_issue_date"],ticket_resolution_proposed_date=j["ticket_resolution_proposed_date"],ticket_details=j['ticket_details'],ticket_resolved_date=j["ticket_resolved_date"],ticket_resolution_response=j["ticket_resolution_response"],ticket_re_action_reason=j["ticket_re_action_reason"],ticket_status=j["ticket_status"],transactions_linked=j['transactions_linked'])
          obj.save()
          w=Ticket.objects.get(ticket_id=j['ticket_id'])
          us=UserProfile.objects.get(user_id=j["userid"])
          us.tickets_linked.add(w)
          us.save()
          return JSONResponse("success")
          # ticket_data=JSONParser().parse(request)
          # ticket_serializer=TicketSerializer(data=ticket_data)
          # if ticket_serializer.is_valid():
          #      ticket_serializer.save()
          # return JSONResponse(ticket_serializer.data,status=status.HTTP_201_CREATED)
          # return JSONResponse(ticket_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     if request.method == "PUT":
          j=json.loads(request.body)
          obj=Ticket.objects.filter(ticket_id=j['ticket_id'])
          obj.update(ticket_resolution_proposed_date=j['ticket_resolution_proposed_date'],ticket_re_action_reason=j["ticket_re_action_reason"],ticket_status=j["ticket_status"])
          return JSONResponse("success")
#@login_required

@csrf_exempt
def messages(request):
     if request.method=='GET':
          MessagesBC=Messages.objects.all()
          MessagesAC=MessagesSerializer(MessagesBC,many=True)
          print(MessagesAC)
          return JSONResponse(MessagesAC.data)

     elif request.method=='POST':
          counter=0
          j=json.loads(request.body)
          print(j)
          obj=Messages(chat_id=j["chat_id"],user_id=j["user_id"],sender_type=j["sender_type"],message_content=j["message_content"],message_type=j["message_type"],time_stamp=j["time_stamp"])
          temp_str=j["message_content"]
          obj.save()
          
          if('transaction' in temp_str.lower() and 'failed' in temp_str.lower()):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please select from below options",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Raise a refund request",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Raise a ticket for transaction done",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
               obj.save()
               counter+=1

          if (('hi'in temp_str.lower())or ('hello'in temp_str.lower())):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Hi, I am voiza, your assistant for the day. How can I help you?",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Payment",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Fault",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="New connection",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="New ticket",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Action on existing tickets",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Other",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
               obj.save()
               counter+=1
          
          if ('payment' in temp_str.lower()):
               if 'failed' in temp_str.lower():
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please select from below options",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Raise a refund request",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Raise a ticket for transaction done",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
                    obj.save()
                    counter+=1

               elif (('payment' in temp_str.lower() and 'not' in temp_str.lower() and 'reflected' in temp_str.lower())or ('payment' in temp_str.lower() and 'not' in temp_str.lower() and 'showing' in temp_str.lower())):
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Not reflected in device",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Not reflected in transactions",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
                    obj.save()
                    counter+=1

               else:
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please select from below options",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Payment failed",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Wrong deduction",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Multiple deduction",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Wrong invoice or no invoice",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
                    obj.save()
                    obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Payment not reflected",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p")))   
                    obj.save()
                    counter+=1

          if 'refund' in temp_str.lower():
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please raise a refund request from your transactions below. If there is an existing request registered with the same transaction, please wait till it get sorted.",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Your transactions",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if 'plans' in temp_str.lower():
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Redirect to plans?",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to plans page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if 'offers' in temp_str.lower():
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Redirect to offers?",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to offers page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('no' in temp_str.lower() and 'invoice' in temp_str.lower()) or ('wrong' in temp_str.lower() and 'invoice' in temp_str.lower())or ('raise' in temp_str.lower() and 'transaction' in temp_str.lower()) or ('wrong' in temp_str.lower() and 'deduction' in temp_str.lower()) or ('multiple' in temp_str.lower() and 'deduction' in temp_str.lower())):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please raise a ticket from your transactions below. If there is an existing ticket registered with the same transaction, please wait till it get sorted.",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Your transactions",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('new' in temp_str.lower() and 'connection' in temp_str.lower()) or ('new' in temp_str.lower() and 'sim' in temp_str.lower()) or ('new' in temp_str.lower() and 'dongle' in temp_str.lower())):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="You will be redirected to new connection page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new connection page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('existing' in temp_str.lower() and 'ticket' in temp_str.lower())):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Your tickets",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('new' in temp_str.lower() and 'ticket' in temp_str.lower()) or ('raise' in temp_str.lower() and 'new' in temp_str.lower() and 'ticket' in temp_str.lower())):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if('other' in temp_str.lower()):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please write to us in detail. We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('device' in temp_str.lower()) and ('not' in temp_str.lower()) and ('reflected' in temp_str.lower())):
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Try rebooting the device. If it persists, please write to us in detail. We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('transactions' in temp_str.lower() or 'transaction' in temp_str.lower()) and ('not' in temp_str.lower()) and ('reflected' in temp_str.lower())):     
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Try refreshing the transactions page. If it persists, please write to us in detail. We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1
               
          if ('fault' in temp_str.lower()):     
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Try rebooting the device. If it persists, please write to us in detail. We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if ('signal' in temp_str.lower()):     
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Try rebooting the device. If it persists, please write to us in detail. We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if (('wrong' in temp_str.lower() and 'bill' in temp_str.lower())or ('no' in temp_str.lower() and 'bill' in temp_str.lower())):     
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Please write to us in detail. We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               counter+=1

          if counter==0:
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Can you please write to us in detail? We are there to help. You will be redirected to new tickets page",message_type="information",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()
               obj=Messages(chat_id=j["chat_id"],user_id="",sender_type="bot",message_content="Ok, redirect me to new ticket page",message_type="option",time_stamp=str(datetime.datetime.now().strftime("%d-%m-%y %I:%M:%S %p"))) 
               obj.save()

     return JSONResponse("success")


# @login_required

@csrf_exempt
def chat(request):
     if request.method=='GET':
          ChatBC=Chat.objects.all()
          ChatAC=ChatSerializer(ChatBC,many=True)
          #print(ChatAC.data)
          print(JSONResponse(ChatAC.data))
          return JSONResponse(ChatAC.data)

     elif request.method=='POST':
          j=json.loads(request.body)
          print(j)
          obj=Chat(user_id=j["user_id"],ip_address=j["ip_address"],start_time=j["start_time"])
          obj.save()
          return JSONResponse("success")