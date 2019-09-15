from djongo import models
from django import forms


class Costing(models.Model):
    flags=models.BooleanField()
    calls=models.CharField( max_length=50)
    data=models.CharField( max_length=50)
    sms=models.CharField( max_length=50)
    
    def __str__(self):
        return self.calls
 
class CostingForm(forms.ModelForm):
    class Meta:
        model = Costing
        fields = (
            '__all__'
        )  


class CostToCompany(models.Model):
    processing= models.CharField(max_length=50)
    gst= models.CharField(max_length=50)
    
    def __str__(self):
        return "" + str(int(self.processing) + int(self.gst))

class CosttoCompanyForm(forms.ModelForm):
    class Meta:
        model = CostToCompany
        fields = (
            '__all__'
        ) 

class Validity(models.Model):
    prepaid_validity= models.CharField(max_length=50)
    postpaid_duration= models.CharField(max_length=50)

    def __str__(self):
        return self.prepaid_validity

class validityForm(forms.ModelForm):
    class Meta:
        model = Validity
        fields = (
            '__all__'
        )

class Plans(models.Model):
    _id = models.ObjectIdField()
    id=models.IntegerField(primary_key=True)
    plans_name = models.CharField(max_length=250)
    plans_price = models.IntegerField()
    plan_type = models.CharField(max_length=50)
    plan_sub_type = models.CharField(max_length=50, blank=True)
    plan_description = models.CharField(max_length=50)
    full_talktime= models.BooleanField()
    validity = models.EmbeddedModelField(model_container = Validity, model_form_class= validityForm)
    costtocompany  = models.EmbeddedModelField(model_container = CostToCompany, model_form_class= CosttoCompanyForm)
    topup_delivered = models.CharField(max_length=50)
    value_delivered =  models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    local= models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    roaming= models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)
    international= models.EmbeddedModelField(model_container = Costing, model_form_class=CostingForm)    
    # different_service_costing= models.EmbeddedModelField(model_container = ClassCosting, model_form_class=ClassCostingForm)


    def __str__(self):
        return self.plans_name

class PlansForm(forms.ModelForm):
    class Meta:
        model = Plans
        fields = (
            '__all__'
        )
