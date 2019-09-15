from rest_framework import serializers
from .models import Accounts, Proofs
from plans.serializers import PlanSerializer,CostingSerializer

class ProofSerializer(serializers.ModelSerializer):
    proof=serializers.FileField()
    class Meta:
        model = Proofs
        fields = (
            'proof',
        ) 


class AccountsSerializer(serializers.ModelSerializer):
    plan_activated = PlanSerializer(many=True)
    current_usage = CostingSerializer()
    proofs_attached=ProofSerializer(many=True)
    class Meta:
        model = Accounts
        fields = (
            'account_type', 'phone_number','plan_activated','current_usage','main_balance', 'expiry','amount_due', 'payment_deadline' , 'proofs_attached', 'circle', 'imei'
        ) 
