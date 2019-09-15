from rest_framework import serializers
from .models import Transactions
from wallet.serializers import WalletSerializer
from card.serializers import CardSerializer
# from accounts.serializers import AccountSerializer


class TransactionsSerializer(serializers.ModelSerializer):
    wallet_linked = WalletSerializer()
    card_linked = CardSerializer()
    
    class Meta:
        model = Transactions
        fields=['transaction_id','invoice_id','transaction_amount','transaction_date_time','transaction_state','payment_mode','bank_name','wallet_linked','card_linked','refund_status','refund_request_status','ticket_status']
    

