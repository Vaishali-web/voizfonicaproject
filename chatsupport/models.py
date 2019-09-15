from django.contrib.auth.models import User
from transaction_history.models import Transactions
from djongo import models

sender_type_choices=(
     ('user','USER'),
     ('bot','BOT'),
)

message_type_choices=(
     ('information','INFORMATION'),
     ('option','OPTION'),
     ('null','NULL')
)

prob_choices = (
    ('info','INFO'),
    ('option','OPTION'),
)

tick_choices = (
    ('Open','OPEN'),
    ('Closed','CLOSED'),
)

class Chat(models.Model):
     _id=models.ObjectIdField()
     chat_id=models.CharField(max_length=100)
     user_id=models.CharField(max_length=100)
     ip_address=models.CharField(max_length=100)
     start_time=models.CharField(max_length=100)

class Messages(models.Model):
     _id=models.ObjectIdField()
     chat_id=models.CharField(max_length=100)
     user_id=models.CharField(max_length=100)
     sender_type=models.CharField(max_length=50,choices=sender_type_choices,default='bot')
     message_content=models.TextField()
     message_type=models.CharField(max_length=50,choices=message_type_choices,default='null')
     time_stamp=models.CharField(max_length=50)

class Ticket(models.Model):
     _id=models.ObjectIdField()
     ticket_id=models.CharField(max_length=100)
     ticket_type=models.CharField(max_length=100)
     ticket_issue_date=models.CharField(max_length=100)
     ticket_resolution_proposed_date=models.CharField(max_length=100)
     ticket_resolved_date=models.CharField(max_length=100,blank=True)
     ticket_details=models.CharField(max_length=1000,blank=True)
     ticket_resolution_response=models.CharField(max_length=100,blank=True)
     ticket_re_action_reason=models.CharField(max_length=100,blank=True)
     ticket_status=models.CharField(max_length=50,choices=tick_choices, default='Open')
     transactions_linked=models.CharField(max_length=100,blank=True)
     

















#from transactions.model import Transactions

# Create your models here.






# class Transactions_for_support(Transactions)
#      refund_status=models.CharField(max_length=50)
#      raise_ticket=models.BooleanField()