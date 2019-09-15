from rest_framework import serializers
from .models import UserProfile
from chatsupport.serializers import TicketSerializer
from card.serializers import CardSerializer
from transaction_history.serializers import TransactionsSerializer
from accounts.serializers import AccountsSerializer
from wallet.serializers import WalletSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    
    accounts_linked= AccountsSerializer(many=True)
    cards_linked = CardSerializer(many=True)
    transactions_linked = TransactionsSerializer(many=True)
    tickets_linked = TicketSerializer(many=True)
    wallets_linked=WalletSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = (
            'first_name','last_name','email_address','phone_number','alternate_phone','kyc_verified','profile_pic','user_joined_date','accounts_linked','tickets_linked','transactions_linked','wallets_linked','cards_linked'
        ) 

        # ,'transactions_linked'