from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from card.models import Card
from wallet.models import Wallet
from .serializers import TransactionsSerializer
import json
from users.models import UserProfile

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content= JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content,**kwargs)

@csrf_exempt
def getTransactions(request):
    if request.method == 'GET':
        trans = Transactions.objects.all()
        trans_serializer =  TransactionsSerializer(trans, many = True)
        return JSONResponse(trans_serializer.data)

    elif request.method == 'POST':
        j=json.loads(request.body)
        if j["payment_mode"]=='Card':
            cardlink=Card.objects.get(card_number=j['card_number'])
            obj=Transactions(invoice_id=j['invoice_id'],transaction_id=j['transaction_id'],transaction_amount=j["transaction_amount"],transaction_date_time=j["transaction_date_time"],transaction_state=j["transaction_state"],payment_mode=j["payment_mode"],card_linked=cardlink,refund_status=j['refund_status'],ticket_status=j['ticket_status'],refund_request_status=j['refund_request_status'])
            obj.save()
            w=Transactions.objects.get(_id=obj.pk)
            us=UserProfile.objects.get(user_id=j["userid"])
            us.transactions_linked.add(w)
            us.save()
            return JSONResponse("success")
                    
        if j["payment_mode"]=='Wallet':
            walletlink=Wallet.objects.get(wallet_auth_id=j['wallet_auth_id'])
            obj=Transactions(invoice_id=j['invoice_id'],transaction_id=j['transaction_id'],transaction_amount=j["transaction_amount"],transaction_date_time=j["transaction_date_time"],transaction_state=j["transaction_state"],payment_mode=j["payment_mode"],wallet_linked=walletlink,refund_status=j['refund_status'],ticket_status=j['ticket_status'],refund_request_status=j['refund_request_status'])
            obj.save()
            w=Transactions.objects.get(_id=obj.pk)
            us=UserProfile.objects.get(user_id=j["userid"])
            us.transactions_linked.add(w)
            us.save()
            return JSONResponse("success")

        if j["payment_mode"]=='Net banking':
            obj=Transactions(invoice_id=j['invoice_id'],transaction_id=j['transaction_id'],transaction_amount=j["transaction_amount"],transaction_date_time=j["transaction_date_time"],transaction_state=j["transaction_state"],payment_mode=j["payment_mode"],bank_name=j['bank_name'],refund_status=j['refund_status'],ticket_status=j['ticket_status'],refund_request_status=j['refund_request_status'])
            obj.save()
            w=Transactions.objects.get(_id=obj.pk)
            us=UserProfile.objects.get(user_id=j["userid"])
            us.transactions_linked.add(w)
            us.save()
            return JSONResponse("success")
    
    elif request.method=='PUT':
        j=json.loads(request.body)
        if j["payment_mode"]=='Card':
            obj=Transactions.objects.filter(transaction_id=j['transaction_id'])
            obj.update(refund_status=j['refund_status'],ticket_status=j['ticket_status'],refund_request_status=j['refund_request_status'])
            return JSONResponse("success")
                    
        if j["payment_mode"]=='Wallet':
            obj=Transactions.objects.filter(transaction_id=j['transaction_id'])
            obj.update(refund_status=j['refund_status'],ticket_status=j['ticket_status'],refund_request_status=j['refund_request_status'])
            return JSONResponse("success")

        if j["payment_mode"]=='Net banking':
            obj=Transactions.objects.filter(transaction_id=j['transaction_id'])
            obj.update(refund_status=j['refund_status'],ticket_status=j['ticket_status'],refund_request_status=j['refund_request_status'])
            return JSONResponse("success")








