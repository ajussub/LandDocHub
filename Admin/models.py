from django.db import models
# from Guest.models import *
# from Office.models import *
# Create your models here.

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)


class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)    
    place_pincode=models.IntegerField(null=True)
    district=models.ForeignKey(tbl_district, on_delete=models.CASCADE,null=True)

    
class tbl_type(models.Model):
    type_name=models.CharField(max_length=50)   

class tbl_services(models.Model):
    services_title=models.CharField(max_length=500)      
    services_details=models.CharField(max_length=500)
    services_criteria=models.CharField(max_length=500)
    services_document=models.FileField(upload_to='Assests/ServiceDocs/')
    
    
class tbl_admin(models.Model):
   admin_name=models.CharField(max_length=50)
   admin_contact=models.IntegerField(null=True)
   admin_email=models.EmailField(max_length=50)   
   admin_password=models.CharField(max_length=50) 


class tbl_knowlederepository(models.Model):
    knowrepo_title=models.CharField(max_length=500)      
    knowrepo_details=models.CharField(max_length=500)
    knowrepo_document=models.FileField(upload_to='Assests/KnowledegeDocs/')

    