from djongo import models
from django import forms
from datetime import datetime

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/proofs', filename)

class Connection(models.Model):
    application_number = models.CharField(max_length=50)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    state= models.CharField(max_length=50)
    zip= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    proof= models.CharField(max_length=50)
    proofnumber= models.CharField(max_length=50)
    proofFile=models.ImageField(upload_to=get_file_path, max_length=None)
    connectiontype= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    dongleselected= models.CharField(max_length=50)
    portin= models.BooleanField()
    current_mobile_number= models.CharField(max_length=50)
    current_network= models.CharField(max_length=50)
    upc= models.CharField(max_length=50)
    requested_date_time= models.CharField(max_length=50)
    status= models.CharField(max_length=50)
    circle= models.CharField(max_length=50)

    def __str__(self):
        return self.first_name



