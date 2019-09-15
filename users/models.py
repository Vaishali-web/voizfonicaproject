from djongo import models
from django import forms
from django.contrib.auth.models import User
from accounts.models import Accounts
from transaction_history.models import Transactions
from chatsupport.models import Ticket
from card.models import Card
from wallet.models import Wallet
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/profile_pic', filename)

class UserProfile(models.Model):
    
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address =models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    alternate_phone = models.CharField(max_length=254)
    kyc_verified = models.BooleanField()
    accounts_linked = models.ArrayReferenceField(to = Accounts, blank=True)
    profile_pic = models.ImageField(upload_to=get_file_path, default='', blank=True, null=True)
    user_joined_date = models.CharField(max_length=50)
    transactions_linked = models.ArrayReferenceField(to = Transactions, on_delete=models.CASCADE, blank=True)
    tickets_linked = models.ArrayReferenceField(to = Ticket, on_delete=models.CASCADE, blank=True)
    cards_linked = models.ArrayReferenceField(to= Card, on_delete=models.CASCADE, blank=True)
    wallets_linked = models.ArrayReferenceField(to= Wallet, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.user.id)
