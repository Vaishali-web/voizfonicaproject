from djongo import models


class Card(models.Model):
    _id=models.ObjectIdField()
    card_holder_name = models.CharField(max_length = 50)
    card_type = models.CharField(max_length = 25)
    card_number = models.CharField(max_length = 50)
    cvv = models.CharField(max_length = 10)
    card_bank = models.CharField(max_length = 50)
    processing_charges=models.CharField(max_length=50)
    card_expiry=models.CharField(max_length=100)




