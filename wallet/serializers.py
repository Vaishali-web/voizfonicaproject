from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wallet
        fields = ['wallet_name','wallet_auth_id','wallet_processing_charges']
