from rest_framework import serializers
from .models import Connection


class ConnectionSerializer(serializers.ModelSerializer):
    proofFile = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = Connection
        fields = (
            'first_name', 'last_name','city','state','zip','email','password','proof','proofnumber','address','portin','current_mobile_number','current_network','upc','status','circle','connectiontype','proofFile','dongleselected','requested_date_time'
        ) 