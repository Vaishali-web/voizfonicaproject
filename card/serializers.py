from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = ['card_holder_name','card_type','card_number','cvv','card_bank','processing_charges','card_expiry']
