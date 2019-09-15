from djongo import models
from wallet.models import Wallet
from card.models import Card

payment_mode_choices=(("Net Banking","Net Banking"),("Card","Card"),("Wallet","Wallet"))
transaction_state_choices=(("Failed","Failed"),("Success","Success"))
class Transactions(models.Model):
    _id=models.ObjectIdField()
    transaction_id=models.CharField(max_length=100)
    invoice_id=models.CharField(max_length=100)
    transaction_amount=models.IntegerField()
    transaction_date_time=models.CharField(max_length=100)
    transaction_state=models.CharField(max_length=50,choices=transaction_state_choices,default="Success")
    payment_mode=models.CharField(max_length=100,choices=payment_mode_choices,default="Net Banking")
    bank_name=models.CharField(max_length=100,blank=True)
    wallet_linked = models.ForeignKey(Wallet, on_delete=models.CASCADE,blank=True)
    card_linked = models.ForeignKey(Card, on_delete=models.CASCADE,blank=True)
    refund_status=models.BooleanField()
    refund_request_status=models.BooleanField()
    ticket_status=models.BooleanField()
    


