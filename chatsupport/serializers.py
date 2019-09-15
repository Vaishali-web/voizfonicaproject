from rest_framework import serializers
from .models import Ticket,Chat,Messages

class ChatSerializer(serializers.ModelSerializer):
     class Meta:
          model=Chat
          fields=['user_id','ip_address','start_time']
class MessagesSerializer(serializers.ModelSerializer):
     class Meta:
          model=Messages
          fields=['chat_id','user_id','sender_type','message_content','message_type','time_stamp']
class TicketSerializer(serializers.ModelSerializer):
     class Meta:
          model=Ticket
          fields=['ticket_id','ticket_type','ticket_issue_date','ticket_resolution_proposed_date','ticket_resolved_date','ticket_details','ticket_resolution_response','ticket_re_action_reason','ticket_status','transactions_linked']