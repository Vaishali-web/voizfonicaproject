from djongo import models
from django import forms
from django.contrib.auth.models import User
import uuid
import os
from plans.models import Costing, CostingForm, Plans

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads', filename)

class Proofs(models.Model):
    _id = models.ObjectIdField()
    proof = models.FileField(upload_to="uploads/", default='', blank=True, null=True)
    
    def __str__(self):
        return os.path.basename(self.proof.name)


class Accounts(models.Model):
    
    _id = models.ObjectIdField()
    account_type = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    plan_activated = models.ArrayReferenceField(to=Plans, on_delete=models.CASCADE, null=True, blank=True)
    current_usage = models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    main_balance = models.FloatField()
    expiry = models.CharField(max_length=50)
    amount_due = models.FloatField()
    payment_deadline = models.CharField(max_length=50)
    proofs_attached = models.ArrayReferenceField(to=Proofs,
        on_delete=models.CASCADE, null=True, blank=True)
    circle = models.CharField(max_length=50)
    imei = models.CharField(max_length=50)

    def __str__(self):
        return str(self.account_type)
