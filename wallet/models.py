from djongo import models


class Wallet(models.Model):
    _id=models.ObjectIdField()
    wallet_name = models.CharField(max_length = 50)
    wallet_auth_id = models.CharField(max_length = 25)
    wallet_processing_charges = models.CharField(max_length = 50)




