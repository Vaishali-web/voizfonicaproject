from djongo import models
from plans.models import Plans
from django.contrib.auth.models import User

class Offer(models.Model):
    _id = models.ObjectIdField()
    offer_banners = models.ImageField(null=True, blank=True, upload_to="uploads/")
    payment_discount = models.FloatField()
    circle = models.CharField(max_length=100)
    offer_valid_till = models.DateTimeField()
    offers_to_users = models.ArrayReferenceField(to=User,on_delete=models.CASCADE, blank=True)
    offered_plans_linked = models.ForeignKey(Plans, on_delete=models.CASCADE)

    def __str__(self):
            return("offer obtained")
   

