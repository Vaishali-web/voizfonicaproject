from rest_framework import serializers
from .models import Plans, Validity, CostToCompany, Costing

class CostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costing
        fields = (
            '__all__'
        )  

class ValiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Validity
        fields = (
            '__all__'
        ) 

class CosttoCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CostToCompany
        fields = (
            '__all__'
        ) 

class PlanSerializer(serializers.ModelSerializer):
    validity = ValiditySerializer()
    costtocompany =CosttoCompanySerializer()
    value_delivered=CostingSerializer()
    
    local=CostingSerializer()
    roaming=CostingSerializer()
    international=CostingSerializer()
    class Meta:
        model = Plans
        fields = (
            'plans_name', 'plans_price','plan_type','plan_sub_type','plan_description', 'full_talktime','topup_delivered', 'value_delivered' , 'validity', 'costtocompany', 'local', 'roaming', 'international'
        ) 
