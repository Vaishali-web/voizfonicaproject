from rest_framework import serializers
from .models import Offer
from plans.serializers import PlanSerializer

class OfferSerializer(serializers.ModelSerializer):
    offered_plans_linked = PlanSerializer()
    class Meta:
        model = Offer
        fields = ['offer_banners','payment_discount','circle','offer_valid_till','offers_to_users', 'offered_plans_linked']




        